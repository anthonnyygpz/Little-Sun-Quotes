from pydantic import BaseModel


class QuoteDesignBase(BaseModel):
    quote_id: int
    design_id: int


class QuoteDesignCreate(QuoteDesignBase):
    pass


class QuoteDesignUpdate(QuoteDesignBase):
    pass


class QuoteDesignResponse(QuoteDesignBase):
    pass

    class Config:
        from_atributtes = True
