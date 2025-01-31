from typing import List, Optional

from sqlalchemy.orm import Session

from little_sun.backend.app.models.sculping_size import SculpingNailSize
from little_sun.backend.app.schemas.sculping_nail_size import (
    SculpingSizeCreate,
    SculpingSizeUpdate,
)


class CRUDSculpingSize:
    def create(self, db: Session, *, obj_in: SculpingSizeCreate) -> SculpingNailSize:
        obj_db = SculpingNailSize(
            size_name=obj_in.size_name,
            description=obj_in.description,
            base_price=obj_in.base_price,
        )
        db.add(obj_db)
        db.commit()
        db.refresh(obj_db)
        return obj_db

    def get_all(self, db: Session) -> List[SculpingNailSize]:
        return db.query(SculpingNailSize).all()

    def get_by_name(self, db: Session, *, name_in: str) -> Optional[SculpingNailSize]:
        return db.query(SculpingNailSize).filter_by(size_name=name_in).first()

    def get_by_id(self, db: Session, *, id: int) -> Optional[SculpingNailSize]:
        return db.query(SculpingNailSize).filter_by(size_id=id).first()

    def update(self, db: Session, *, obj_in: SculpingSizeUpdate):
        obj_sculping_size = {}
        if obj_in.size_name != "":
            obj_sculping_size["size_name"] = obj_in.size_name
        if obj_in.description != "":
            obj_sculping_size["description"] = obj_in.description
        if obj_in.base_price != 0:
            obj_sculping_size["base_price"] = obj_in.base_price

        if obj_sculping_size:
            db.query(SculpingNailSize).filter_by(size_id=obj_in.size_id).update(
                obj_sculping_size
            )
            return {"message": "Datos actualizados"}

        return {"message": "No actulizo nada"}

    def delete(self, db: Session, *, id: int):
        return db.query(SculpingNailSize).filter_by(size_id=id).delete()


crud_sculping_size = CRUDSculpingSize()
