from dataclasses import dataclass

from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..db.models.clients_model import Clients
from ..schemas.client import CreateClientsSchema


@dataclass()
class ClientsDB:
    db: Session

    def register_clients_db(self, client: CreateClientsSchema):
        try:
            db_query = Clients(**client.model_dump())
            self.db.add(db_query)
            self.db.commit()
            self.db.refresh(db_query)

            return db_query
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_clients_db(self):
        try:
            db_query = self.db.query(Clients).all()
            return db_query
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_one_client_db(self, name: str):
        try:
            db_query = self.db.query(Clients).filter(Clients.name == name).all()
            return db_query
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
