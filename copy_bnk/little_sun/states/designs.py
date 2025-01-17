from typing import Dict, List
import reflex as rx
from little_sun.services.api_clients import logger, DataFetchError, DataFetcher


class DesingsAPI:
    def __init__(self, base_url: str = "http://0.0.0.0:8000"):
        self.fetcher = DataFetcher(base_url, cache_ttl=1800)
        self.list_endpoint = "/api/get_design"

    async def get_quotes(self) -> List[Dict]:
        async with self.fetcher as fetcher:
            response = await fetcher.fetch_data(self.list_endpoint)
            return response.data  # type: ignore


class DesignsState(rx.State):
    selected: list[str] = []

    data: List[Dict] = []
    loading: bool = False
    error: str = ""

    async def fetch_data(self):
        self.loading = True
        api = DesingsAPI()
        try:
            # logger.info("Fetching user 1 (second time)...")
            desings = await api.get_quotes()
            self.data = desings
        except DataFetchError as he:
            self.error = f"{str(he)}"
        finally:
            self.loading = False

    def on_mount(self):
        self.selected = []

    @rx.event
    def handle_select(self, value: str):
        if value in self.selected:
            self.selected.remove(value)
        else:
            self.selected.append(value)


#
