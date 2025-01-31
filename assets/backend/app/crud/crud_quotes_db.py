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
                    func.string_agg(distinct(Services.service_name), ", ").label(
                        "services"
                    ),  # Agregado separador
                    func.string_agg(distinct(Designs.design_name), ", ").label(
                        "designs"
                    ),  # Agregado separador
                    Quotes.total_amount,
                    Quotes.status,
                    Quotes.created_at,
                )
                .join(Clients, Quotes.client_id == Clients.client_id)
                .outerjoin(NailSizes, Quotes.nail_size_id == NailSizes.size_id)
                .outerjoin(QuoteServices, Quotes.quote_id == QuoteServices.quote_id)
                .outerjoin(Services, QuoteServices.service_id == Services.service_id)
                .outerjoin(QuoteDesigns, Quotes.quote_id == QuoteDesigns.quote_id)
                .outerjoin(Designs, QuoteDesigns.design_id == Designs.design_id)
                .group_by(
                    Quotes.quote_id,
                    Quotes.client_id,
                    Clients.name,
                    Clients.phone_number,
                    NailSizes.size_name,
                    Quotes.nail_size_id,
                    Quotes.total_amount,
                    Quotes.status,
                    Quotes.created_at,
                )
                .order_by(Quotes.created_at.desc())
                .all()
            )
            # Removemos la validación de datos vacíos para permitir listas vacías
            return [
                {
                    "quote_id": query.quote_id,
                    "client_id": query.client_id,
                    "name": query.client_name,
                    "size_name": query.size_name if query.size_name else "",
                    "phone": query.phone_number,
                    "services": query.services if query.services else "",
                    "designs": query.designs if query.designs else "",
                    "total_amount": query.total_amount,
                    "status": query.status,
                    "created_at": query.created_at,
                    "size_id": query.nail_size_id if query.nail_size_id else 0,
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
            # Crear diccionario solo con campos no vacíos para Quotes
            update_fields = {}
            if quote.client_id != 0:
                update_fields["client_id"] = quote.client_id
            if quote.nail_size_id != 0:
                update_fields["nail_size_id"] = quote.nail_size_id
            if quote.total_amount != 0:
                update_fields["total_amount"] = quote.total_amount
            if quote.status != "":
                update_fields["status"] = quote.status

            # Actualizar solo si hay campos para actualizar
            if update_fields:
                self.db.query(Quotes).filter_by(quote_id=quote.quote_id).update(
                    update_fields
                )

            # Quote Designs - verificar si existen registros
            existing_designs = (
                self.db.query(QuoteDesigns).filter_by(quote_id=quote.quote_id).all()
            )

            if quote.designs != []:
                # Si hay diseños existentes, eliminarlos
                if existing_designs:
                    self.db.query(QuoteDesigns).filter_by(
                        quote_id=quote.quote_id
                    ).delete()
                # Agregar nuevos diseños
                for id in quote.designs:
                    add_quote_designs = QuoteDesigns(
                        quote_id=quote.quote_id, design_id=id
                    )
                    self.db.add(add_quote_designs)
            elif not existing_designs:
                # Si no hay diseños existentes y no se proporcionaron nuevos, crear uno vacío
                add_quote_designs = QuoteDesigns(
                    quote_id=quote.quote_id,
                    design_id=0,  # O el valor predeterminado que prefieras
                )
                self.db.add(add_quote_designs)

            # Quote Services - verificar si existen registros
            existing_services = (
                self.db.query(QuoteServices).filter_by(quote_id=quote.quote_id).all()
            )

            if quote.services != []:
                # Si hay servicios existentes, eliminarlos
                if existing_services:
                    self.db.query(QuoteServices).filter_by(
                        quote_id=quote.quote_id
                    ).delete()
                # Agregar nuevos servicios
                for id in quote.services:
                    add_quote_services = QuoteServices(
                        quote_id=quote.quote_id, service_id=id
                    )
                    self.db.add(add_quote_services)
            elif not existing_services:
                # Si no hay servicios existentes y no se proporcionaron nuevos, crear uno vacío
                add_quote_services = QuoteServices(
                    quote_id=quote.quote_id,
                    service_id=0,  # O el valor predeterminado que prefieras
                )
                self.db.add(add_quote_services)

            # Actualizar cliente solo si los campos no son None
            client_update = {}
            if quote.name != "":
                client_update["name"] = quote.name
            if quote.phone_number != 0:
                client_update["phone_number"] = quote.phone_number

            if client_update:
                self.db.query(Clients).filter_by(client_id=quote.client_id).update(
                    client_update
                )

            self.db.commit()
            self.db.close()
            return {"message": "Datos actualizados"}
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
