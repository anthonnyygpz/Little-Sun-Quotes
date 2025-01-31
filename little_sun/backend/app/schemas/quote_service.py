from typing import Optional
from pydantic import BaseModel


class QuoteServiceBase(BaseModel):
    quote_id: Optional[int]
    service_id: Optional[int]


class QuoteServiceCreate(QuoteServiceBase):
    pass


class QuoteServiceUpdate(QuoteServiceBase):
    pass


class QuoteServiceResponse(QuoteServiceBase):
    pass

    class Config:
        from_atributtes = True
