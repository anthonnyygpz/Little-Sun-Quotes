from dataclasses import dataclass

from fastapi import HTTPException
from sqlalchemy.orm import Session

from ..db.models.quotes_model import Quotes
from ..schemas.quote_schema import CreateQuotesSchema
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
                    Clients.name.label("client_name"),
                    Clients.phone_number,
                    NailSizes.size_name,
                    func.group_concat(distinct(Services.service_name)).label(
                        "services"
                    ),
                    func.group_concat(distinct(Designs.design_name)).label(
                        "designs"
                    ),
                    Quotes.total_amount,
                    Quotes.created_at,
                )
                .join(Clients, Quotes.client_id == Clients.client_id)
                .join(NailSizes, Quotes.nail_size_id == NailSizes.size_id)
                .join(QuoteServices, Quotes.quote_id == QuoteServices.quote_id)
                .join(Services, QuoteServices.service_id == Services.service_id)
                .join(QuoteDesigns, Quotes.quote_id == QuoteDesigns.quote_id)
                .join(Designs, QuoteDesigns.design_id == Designs.design_id)
                .filter(Quotes.status == "pending")
                .group_by(Quotes.quote_id)
                .order_by(Quotes.created_at.desc())
                .all()
            )
            if not db_query:
                raise HTTPException(
                    status_code=404, detail="No pending quotes found"
                )

            return [
                {
                    "quote_id": query.quote_id,
                    "name": query.client_name,
                    "size_name": query.size_name,
                    "services": [query.services],
                    "designs": [query.designs],
                    "total_amount": query.total_amount,
                    "created_at": query.created_at,
                }
                for query in db_query
            ]
        except SQLAlchemyError as e:
            raise HTTPException(
                status_code=500, detail=f"Database error: {str(e)}"
            )
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"An unexpected error occurred: {str(e)}",
            )
