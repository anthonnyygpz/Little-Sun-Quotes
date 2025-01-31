from typing import Optional
from pydantic import BaseModel


class SculpingSizeBase(BaseModel):
    size_name: str
    description: Optional[str]
    base_price: int


class SculpingSizeCreate(SculpingSizeBase):
    pass


class SculpingSizeUpdate(SculpingSizeBase):
    size_id: int


class SculpingSizeResponse(SculpingSizeBase):
    size_id: int

    class Config:
        from_atributtes = True
