from typing import List, Optional

from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from little_sun.backend.app.models.design import Design
from little_sun.backend.app.schemas.design import DesignCreate, DesignUpdate


class CRUDDesign:
    def create(self, db: Session, *, obj_in: DesignCreate) -> Design:
        try:
            obj_db = Design(
                design_name=obj_in.design_name,
                description=obj_in.description,
                price=obj_in.price,
            )
            db.add(obj_db)
            db.commit()
            db.refresh(obj_db)
            return obj_db
        except SQLAlchemyError as he:
            db.rollback()
            raise HTTPException(status_code=400, detail=str(he))
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=404, detail=str(e))

    def get_all(self, db: Session) -> Optional[List[Design]]:
        return db.query(Design).all()

    def get_by_name(self, db: Session, *, name_in: str) -> Optional[Design]:
        return db.query(Design).filter_by(design_name=name_in).first()

    def get_by_id(self, db: Session, *, design_id: int) -> Optional[Design]:
        return db.query(Design).filter_by(design_id=design_id).first()

    def update(self, db: Session, *, obj_in: DesignUpdate):
        obj_design = {}
        if obj_in.design_name != "":
            obj_design["design_name"] = obj_in.design_name
        if obj_in.description != "":
            obj_design["description"] = obj_in.description
        if obj_in.price != 0:
            obj_design["price"] = obj_in.price
        if obj_design:
            db.query(Design).filter_by(design_id=obj_in.design_id).update(obj_design)
        db.commit()
        db.close()
        return {"message": "Datos actualizados"}

    def delete(self, db: Session, *, design_id: int):
        obj_db = db.query(Design).filter_by(design_id=design_id).delete()
        db.commit()
        return obj_db


crud_design = CRUDDesign()
