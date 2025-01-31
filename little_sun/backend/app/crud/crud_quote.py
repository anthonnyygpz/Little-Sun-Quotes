from typing import Dict, List, Optional

from sqlalchemy import distinct, func
from sqlalchemy.orm import Session

from little_sun.backend.app.models.client import Client
from little_sun.backend.app.models.design import Design
from little_sun.backend.app.models.quote import Quote
from little_sun.backend.app.models.quote_design import QuoteDesign
from little_sun.backend.app.models.quote_service import QuoteService
from little_sun.backend.app.models.sculping_size import SculpingNailSize
from little_sun.backend.app.models.service import Service
from little_sun.backend.app.schemas.quote import QuoteCreate, QuoteUpdate


class CRUDQuote:
    def create(self, db: Session, *, obj_in: QuoteCreate) -> Quote:
        obj_db = Quote(
            client_id=obj_in.client_id,
            nail_size_id=obj_in.nail_size_id,
            total_amount=obj_in.total_amount,
        )
        db.add(obj_db)
        db.commit()
        db.refresh(obj_db)
        return obj_db

    def get_all(self, db: Session) -> List[Dict]:
        obj_db = (
            db.query(
                Quote.quote_id,
                Quote.client_id,
                Client.name.label("client_name"),
                Client.phone_number,
                SculpingNailSize.size_name,
                Quote.nail_size_id,
                func.string_agg(distinct(Service.service_name), ", ").label("services"),
                func.string_agg(distinct(Design.design_name), ", ").label("designs"),
                Quote.total_amount,
                Quote.status,
                Quote.created_at,
            )
            .outerjoin(Client, Quote.client_id == Client.client_id)
            .outerjoin(SculpingNailSize, Quote.nail_size_id == SculpingNailSize.size_id)
            .outerjoin(QuoteService, Quote.quote_id == QuoteService.quote_id)
            .outerjoin(Service, QuoteService.service_id == Service.service_id)
            .outerjoin(QuoteDesign, Quote.quote_id == QuoteDesign.quote_id)
            .outerjoin(Design, QuoteDesign.design_id == Design.design_id)
            .group_by(
                Quote.quote_id,
                Quote.client_id,
                Client.name,
                Client.phone_number,
                SculpingNailSize.size_name,
                Quote.nail_size_id,
                Quote.total_amount,
                Quote.status,
                Quote.created_at,
            )
            .order_by(Quote.created_at.desc())
            .all()
        )

        return [
            {
                "quote_id": query.quote_id,
                "client_id": query.client_id,
                "name": query.client_name,
                "size_name": query.size_name if query.size_name else "",
                "phone_number": query.phone_number,
                "services": query.services if query.services else "",
                "designs": query.designs if query.designs else "",
                "total_amount": query.total_amount,
                "status": query.status,
                "created_at": query.created_at,
                "nail_size_id": query.nail_size_id if query.nail_size_id else 0,
            }
            for query in obj_db
        ]

    def get_by_id(self, db: Session, *, id: int) -> Optional[Quote]:
        return db.query(Quote).filter_by(quote_id=id).first()

    def update(self, db: Session, *, obj_in: QuoteUpdate) -> Dict:
        obj_quote = {}
        if obj_in.client_id != 0:
            obj_quote["client_id"] = obj_in.client_id
        if obj_in.nail_size_id != 0:
            obj_quote["nail_size_id"] = obj_in.nail_size_id
        if obj_in.total_amount != 0:
            obj_quote["total_amount"] = obj_in.total_amount
        if obj_in.status != "":
            obj_quote["status"] = obj_in.status
        if obj_quote:
            db.query(Quote).filter_by(quote_id=obj_in.quote_id).update(obj_quote)
            db.commit()

        existing_designs = (
            db.query(QuoteDesign).filter_by(quote_id=obj_in.quote_id).all()
        )

        if obj_in.designs != []:
            if existing_designs:
                db.query(QuoteDesign).filter_by(quote_id=obj_in.quote_id).delete()

            for id in obj_in.designs:
                add_obj_designs = QuoteDesign(quote_id=obj_in.quote_id, design_id=id)
                db.add(add_obj_designs)
                db.commit()
                db.refresh(add_obj_designs)

        elif not existing_designs:
            add_obj_designs = QuoteDesign(quote_id=obj_in.quote_id, design_id=0)
            db.add(add_obj_designs)
            db.commit()
            db.refresh(add_obj_designs)

        existing_services = (
            db.query(QuoteService).filter_by(quote_id=obj_in.quote_id).all()
        )

        if obj_in.services != []:
            if existing_services:
                db.query(QuoteService).filter_by(quote_id=obj_in.quote_id).delete()
            for id in obj_in.services:
                add_obj_services = QuoteService(quote_id=obj_in.quote_id, service_id=id)
                db.add(add_obj_services)
                db.commit()
                db.refresh(add_obj_services)

        elif not existing_services:
            add_obj_services = QuoteService(quote_id=obj_in.quote_id, service_id=0)
            db.add(add_obj_services)
            db.commit()
            db.refresh(add_obj_services)

        obj_client = {}
        if obj_in.name != "":
            obj_client["name"] = obj_in.name
        if obj_in.phone_number != 0:
            obj_client["phone_number"] = obj_in.phone_number

        if obj_client:
            db.query(Client).filter_by(client_id=obj_in.client_id).update(obj_client)
            db.commit()

        return {"message": "Datos actulizados"}

    def delete(self, db: Session, *, id: int):
        obj_quote = db.query(Quote).filter_by(quote_id=id).delete()
        db.commit()
        return obj_quote


crud_quote = CRUDQuote()
