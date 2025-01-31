from sqlalchemy.orm import Session

from little_sun.backend.app.models.quote_design import QuoteDesign
from little_sun.backend.app.schemas.quote_design import QuoteDesignCreate


class CRUDQuoteDesign:
    def create(self, db: Session, *, obj_in: QuoteDesignCreate):
        obj_db = QuoteDesign(quote_id=obj_in.quote_id, design_id=obj_in.design_id)
        db.add(obj_db)
        db.commit()
        db.refresh(obj_db)
        return obj_db


crud_quote_design = CRUDQuoteDesign()
