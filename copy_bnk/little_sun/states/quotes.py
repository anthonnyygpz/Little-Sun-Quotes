from typing import Dict

from pydantic import BaseModel
from little_sun.services.api_clients import DataFetcher


class CreateQuotes(BaseModel):
    client_id: int
    nail_size_id: int
    total_amount: int


class QuotesApi:
    def __init__(self, base_url: str = "http://0.0.0.0:8000"):
        self.fetcher = DataFetcher(base_url, cache_ttl=1800)

    async def create(self, quote: CreateQuotes) -> Dict:
        async with self.fetcher as fetcher:
            response = await fetcher.fetch_data(
                "/api/create_quotes",
                method="POST",
                data=quote.model_dump(),
                use_cache=False,
            )
            return response.data  # type: ignore
