from typing import Dict
import asyncio

from api_clients import logger, DataFetchError, DataFetcher


class UserAPI:
    def __init__(self, base_url: str = "http://0.0.0.0:8000/api/"):
        self.fetcher = DataFetcher(base_url, cache_ttl=1800)  # 30 minutos de caché

    async def get_quotes(self) -> Dict:
        async with self.fetcher as fetcher:
            response = await fetcher.fetch_data("get_quotes_data")
            return response.data  # type: ignore


async def main():
    user_api = UserAPI()

    try:
        logger.info("Fetching user 1 (second time)...")
        user = await user_api.get_quotes()
        print(user)
    except DataFetchError as e:
        print(f"Error: {e.message}")
        if e.status_code:
            print(f"Status code: {e.status_code}")


if __name__ == "__main__":
    asyncio.run(main())
