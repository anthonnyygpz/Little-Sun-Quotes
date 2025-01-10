from typing import Dict, List

import reflex as rx

from little_sun.services.api_clients import DataFetcher, DataFetchError, logger


class QuoteAPI:
    def __init__(self, base_url: str = "http://0.0.0.0:8000"):
        self.fetcher = DataFetcher(base_url, cache_ttl=1800)
        self.list_endpoint = "/api/get_quotes_data"
        self.delete_endpoint = "/api/delete_quote"

    async def get_quotes(self) -> List[Dict]:
        async with self.fetcher as fetcher:
            response = await fetcher.fetch_data(self.list_endpoint)
            return response.data  # type: ignore

    async def delete_quote(self, quote_id: int) -> bool:
        async with self.fetcher as fetcher:
            response = await fetcher.fetch_data(
                endpoint=self.delete_endpoint,
                method="DELETE",
                params={"quote_id": quote_id},
                update_list_cache=True,
                list_endpoint=self.list_endpoint,
            )
            return response.success


class CRUDDashboard(rx.State):
    user: List[Dict] = []
    successfully_delete: str = ""
    add_services: List[Dict] = []

    def on_mount(self):
        self.add_services = []

    @rx.event(background=True)
    async def view_quotes(self):
        quotes_api = QuoteAPI()
        async with self:
            try:
                logger.info("Fetching user 1 (second time)...")
                quotes = await quotes_api.get_quotes()
                if quotes == None:
                    self.user = []
                    return
                self.user = quotes  # type: ignore
            except DataFetchError as e:
                print(f"Error: {e.message}")
                if e.status_code:
                    print(f"Status code: {e.status_code}")
                self.user = []
                return

    @rx.event
    async def delete_quotes(self, quote_id: int):
        quotes_api = QuoteAPI()
        try:
            await quotes_api.delete_quote(quote_id)
            self.successfully_delete = "Se elimino correctamnete"
            yield

        except DataFetchError as e:
            self.successfully_delete = str(e)

    def add_is_true(self, is_true):
        print(is_true)

    def add(self, id, is_true):
        self.add_services.append({"id": id, "is_true": is_true})

    @rx.event
    def update_quotes(self, form_data: Dict):
        print(form_data)
