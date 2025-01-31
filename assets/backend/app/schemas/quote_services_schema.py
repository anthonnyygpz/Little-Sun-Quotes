from pydantic import BaseModel


class QuoteServicesBase(BaseModel):
    pass


class CreateQuoteServicesSchema(QuoteServicesBase):
    quote_id: int
    service_id: int
