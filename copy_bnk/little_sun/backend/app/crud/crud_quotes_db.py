from dataclasses import dataclass

from fastapi import HTTPException
from sqlalchemy.orm import Session

from ..db.models.quotes_model import Quotes
from ..schemas.quote_schema import CreateQuotesSchema, UpdateQuoteSchema
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import func, distinct

from ..db.models.clients_model import Clients
from ..db.models.nail_sizes_models import NailSizes
from ..db.models.designs_model import Designs
from ..db.models.services_models import Services
from ..db.models.quote_designs_model import QuoteDesigns
from ..db.models.quote_services_model import QuoteServices


@dataclass
class QuotesDB:
    db: Session

    def create_quotes_db(self, quote: CreateQuotesSchema):
        try:
            db_query = Quotes(**quote.model_dump())
            self.db.add(db_query)
            self.db.commit()
            self.db.refresh(db_query)
            return db_query
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_quote_data_db(self):
        try:
            db_query = (
                self.db.query(
                    Quotes.quote_id,
                    Quotes.client_id,
                    Clients.name.label("client_name"),
                    Clients.phone_number,
                    NailSizes.size_name,
                    Quotes.nail_size_id,
                    func.group_concat(distinct(Services.service_name)).label(
                        "services"
                    ),
                    func.group_concat(distinct(Designs.design_name)).label("designs"),
                    Quotes.total_amount,
                    Quotes.status,
                    Quotes.created_at,
                )
                .join(Clients, Quotes.client_id == Clients.client_id)
                .join(NailSizes, Quotes.nail_size_id == NailSizes.size_id)
                .join(QuoteServices, Quotes.quote_id == QuoteServices.quote_id)
                .join(Services, QuoteServices.service_id == Services.service_id)
                .join(QuoteDesigns, Quotes.quote_id == QuoteDesigns.quote_id)
                .join(Designs, QuoteDesigns.design_id == Designs.design_id)
                # .filter(Quotes.status == "pending")
                .group_by(Quotes.quote_id)
                .order_by(Quotes.created_at.desc())
                .all()
            )
            if not db_query:
                raise HTTPException(status_code=404, detail="No pending quotes found")

            return [
                {
                    "quote_id": query.quote_id,
                    "client_id": query.client_id,
                    "name": query.client_name,
                    "size_name": query.size_name,
                    "phone": query.phone_number,
                    "services": query.services,
                    "designs": query.designs,
                    "total_amount": query.total_amount,
                    "status": query.status,
                    "created_at": query.created_at,
                    "size_id": query.nail_size_id,
                }
                for query in db_query
            ]
        except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"An unexpected error occurred: {str(e)}",
            )

    def update_quotes_db(self, quote: UpdateQuoteSchema):
        try:
            self.db.query(Quotes).filter_by(quote_id=quote.quote_id).update(
                {
                    "client_id": quote.client_id,
                    "nail_size_id": quote.nail_size_id,
                    "total_amount": quote.total_amount,
                    "status": quote.status,
                }
            )

            # Quote Designs
            self.db.query(QuoteDesigns).filter_by(quote_id=quote.quote_id).delete()
            for id in quote.designs:  # type: ignore
                add_quote_designs = QuoteDesigns(quote_id=quote.quote_id, design_id=id)
                self.db.add(add_quote_designs)

            # Quote Services
            self.db.query(QuoteServices).filter_by(quote_id=quote.quote_id).delete()
            for id in quote.services:
                add_quote_services = QuoteServices(
                    quote_id=quote.quote_id, service_id=id
                )
                self.db.add(add_quote_services)

            self.db.query(Clients).filter_by(client_id=quote.client_id).update(
                {"name": quote.name}
            )

            self.db.commit()
            self.db.close()

            return {"message": "Datos actualizaddos"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def delete_quote_db(self, quote_id: int):
        try:
            db_query = self.db.query(Quotes).filter(Quotes.quote_id == quote_id).first()
            self.db.delete(db_query)
            self.db.commit()
            return {"message": "Se elimino correctamente"}

        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
