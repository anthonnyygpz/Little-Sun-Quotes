from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException

from little_sun.backend.app.schemas.client import ClientCreate
from little_sun.backend.app.models.client import Client


class CRUDClient:
    def create(self, db: Session, *, obj_in: ClientCreate) -> Client:
        try:
            obj_db = Client(
                name=obj_in.name,
                phone_number=obj_in.phone_number,
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

    def get_by_name(self, db: Session, *, name: str) -> Optional[Client]:
        return db.query(Client).filter_by(name=name).first()

    def get_all(self, db: Session):
        obj_db = db.query(Client).all()
        return obj_db


crud_client = CRUDClient()
