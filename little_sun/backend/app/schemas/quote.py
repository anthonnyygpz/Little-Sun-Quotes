from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class QuoteBase(BaseModel):
    client_id: Optional[int]
    nail_size_id: Optional[int]
    name: Optional[str]
    phone_number: Optional[int]
    total_amount: Optional[int]
    designs: Optional[List[int]]
    services: Optional[List[int]]


class QuoteCreate(BaseModel):
    client_id: Optional[int]
    nail_size_id: Optional[int]
    total_amount: Optional[int]


class QuoteUpdate(QuoteBase):
    quote_id: int
    client_id: Optional[int]
    status: Optional[str]


class QuoteResponse(QuoteBase):
    size_name: str
    created_at: datetime

    class Config:
        from_atributtes = True
