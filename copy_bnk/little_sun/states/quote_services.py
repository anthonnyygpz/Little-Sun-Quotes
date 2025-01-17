from pydantic import BaseModel
from little_sun.services.api_clients import DataFetcher
from typing import Dict


class QuoteServicesCreate(BaseModel):
    quote_id: int
    service_id: int


class QuoteServicesApi:
    def __init__(self, base_url: str = "http://0.0.0.0:8000"):
        self.fetcher = DataFetcher(base_url, cache_ttl=18000)

    async def create(self, quote_service: QuoteServicesCreate) -> Dict:
        async with self.fetcher as fetcher:
            response = await fetcher.fetch_data(
                "/api/create_quote_services",
                method="POST",
                data=quote_service.model_dump(),
                use_cache=False,
            )
            return response.data  # type: ignore
