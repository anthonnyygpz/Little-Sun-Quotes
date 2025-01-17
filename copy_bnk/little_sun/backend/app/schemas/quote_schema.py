from typing import List, Optional
from pydantic import BaseModel


class QuotesBase(BaseModel):
    pass


class CreateQuotesSchema(QuotesBase):
    client_id: Optional[int]
    nail_size_id: Optional[int]
    total_amount: Optional[int]


class UpdateQuoteSchema(QuotesBase):
    quote_id: int
    client_id: int
    name: str
    nail_size_id: int
    total_amount: int
    status: str
    designs: List[int]
    services: List[int]
