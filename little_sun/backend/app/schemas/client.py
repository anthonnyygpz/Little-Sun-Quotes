from typing import Optional
from pydantic import BaseModel


class ClientBase(BaseModel):
    pass


class CreateClientsSchema(BaseModel):
    name: str
    phone_number: Optional[str]
