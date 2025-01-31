from typing import Optional
from pydantic import BaseModel


class DesignBase(BaseModel):
    design_name: str
    description: Optional[str]
    price: int


class DesignCreate(DesignBase):
    pass


class DesignUpdate(DesignBase):
    design_id: int


class DesignResponse(DesignBase):
    design_id: int

    class Config:
        from_atributtes = True
