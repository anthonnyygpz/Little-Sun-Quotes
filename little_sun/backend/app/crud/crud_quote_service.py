from sqlalchemy.orm import Session

from little_sun.backend.app.models.quote_service import QuoteService
from little_sun.backend.app.schemas.quote_service import QuoteServiceCreate


class CRUDQuoteService:
    def create(self, db: Session, *, obj_in: QuoteServiceCreate):
        obj_db = QuoteService(quote_id=obj_in.quote_id, service_id=obj_in.service_id)
        db.add(obj_db)
        db.commit()
        db.refresh(obj_db)
        return obj_db


crud_quote_service = CRUDQuoteService()
