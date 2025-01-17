from dataclasses import dataclass

from fastapi import HTTPException
from sqlalchemy.orm import Session

from little_sun.backend.app.schemas.client import CreateClientsSchema
from ..crud.crud_clients import ClientsDB


@dataclass()
class ClientsRepositories:
    db: Session

    def register_clients_repositories(self, client: CreateClientsSchema):
        try:
            return ClientsDB(self.db).register_clients_db(client)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    def get_clients_repositories(self):
        try:
            return ClientsDB(self.db).get_clients_db()
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    def get_one_client_repositories(self, name: str):
        try:
            return ClientsDB(self.db).get_one_client_db(name)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
