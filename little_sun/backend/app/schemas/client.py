from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class ClientBase(BaseModel):
    name: Optional[str]
    phone_number: Optional[int]


class ClientCreate(ClientBase):
    pass


class ClientUpdate(ClientBase):
    pass


class ClientResponse(ClientBase):
    client_id: int
    created_at: datetime

    class Config:
        from_atributtes = True
