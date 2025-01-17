from pydantic import BaseModel
from little_sun.services.api_clients import DataFetcher
from typing import Dict


class QuoteDesignsCreate(BaseModel):
    quote_id: int
    design_id: int


class QuotDesignsApi:
    def __init__(self, base_url: str = "http://0.0.0.0:8000"):
        self.fetcher = DataFetcher(base_url, cache_ttl=18000)

    async def create(self, quote_design: QuoteDesignsCreate) -> Dict:
        async with self.fetcher as fetcher:
            response = await fetcher.fetch_data(
                "/api/create_quote_designs",
                method="POST",
                data=quote_design.model_dump(),
                use_cache=False,
            )
            return response.data  # type: ignore
