from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException

from little_sun.backend.app.models.service import Service
from little_sun.backend.app.schemas.service import ServiceCreate, ServiceUpdate


class CRUDService:
    def create(self, db: Session, *, obj_in: ServiceCreate) -> Service:
        try:
            obj_db = Service(
                service_name=obj_in.service_name,
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

    def get_all(self, db: Session) -> Optional[List[Service]]:
        return db.query(Service).all()

    def get_by_name(self, db: Session, *, name_in: str) -> Optional[Service]:
        return db.query(Service).filter_by(service_name=name_in).first()

    def get_by_id(self, db: Session, *, service_id: int) -> Optional[Service]:
        return db.query(Service).filter_by(service_id=service_id).first()

    def update(self, db: Session, *, obj_in: ServiceUpdate):
        obj_service = {}
        if obj_in.service_name != "":
            obj_service["service_name"] = obj_in.service_name
        if obj_in.description != "":
            obj_service["description"] = obj_in.description
        if obj_in.price != 0:
            obj_service["price"] = obj_in.price
        if obj_service:
            db.query(Service).filter_by(service_id=obj_in.service_id).update(
                obj_service
            )
        db.commit()
        db.close()
        return {"message": "Datos actualizados"}

    def delete(self, db: Session, *, service_id: int):
        obj_db = db.query(Service).filter_by(service_id=service_id).delete()
        db.commit()
        return obj_db


crud_service = CRUDService()
