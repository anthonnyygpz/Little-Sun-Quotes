from typing import Optional
from pydantic import BaseModel


class ServiceBase(BaseModel):
    service_name: str
    description: Optional[str]
    price: int


class ServiceCreate(ServiceBase):
    pass


class ServiceUpdate(ServiceBase):
    service_id: int


class ServiceResponse(ServiceBase):
    service_id: int

    class Config:
        from_atributtes = True
