from typing import Optional
from pydantic import BaseModel


class QuotesBase(BaseModel):
    pass


class CreateQuotesSchema(QuotesBase):
    client_id: Optional[int]
    nail_size_id: Optional[int]
    total_amount: Optional[int]
