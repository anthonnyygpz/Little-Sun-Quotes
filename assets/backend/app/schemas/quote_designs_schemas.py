from pydantic import BaseModel


class QuoteDeginsBase(BaseModel):
    pass


class CreateQuoteDesignsSchema(QuoteDeginsBase):
    quote_id: int
    design_id: int
