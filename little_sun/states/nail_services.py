from typing import Dict, List
import reflex as rx
from little_sun.services.api_clients import logger, DataFetchError, DataFetcher


class ServicesApi:
    def __init__(self, base_url: str = "http://0.0.0.0:8000"):
        self.fetcher = DataFetcher(base_url, cache_ttl=1800)
        self.list_endpoint = "/api/get_nail_services"

    async def get_services(self) -> List[Dict]:
        async with self.fetcher as fetcher:
            response = await fetcher.fetch_data(self.list_endpoint)
            return response.data  # type: ignore


class ServicesState(rx.State):
    items: List[Dict] = []
    total_price: int = 0
    all_checked: List = []
    is_checked: Dict[str, bool] = {
        checkbox_name: False for checkbox_name in all_checked
    }

    data: List[Dict] = []
    error: str = ""
    loading: bool = False

    async def fetch_data(self):
        self.loading = True
        api = ServicesApi()
        try:
            # logger.info("Fetching user 1 (second time)...")
            services = await api.get_services()
            self.data = services
        except DataFetchError as he:
            self.error = f"{str(he)}"
        except Exception as e:
            self.error = f"Error fetching data: {str(e)}"
        finally:
            self.loading = False

    def on_mount(self):
        self.items = []
        self.total_price = 0
        self.is_checked = {checkbox_name: False for checkbox_name in self.all_checked}

    def toggle_checked(self, checkbox_name: str) -> None:
        self.all_checked = [item["name"] for item in self.items]

        if checkbox_name not in self.is_checked:
            self.is_checked[checkbox_name] = False

        self.is_checked[checkbox_name] = not self.is_checked.get(checkbox_name, False)

    @rx.event
    def toggle_item(self, name: str, price: int, id, category):
        if name in [item["name"] for item in self.items]:
            self.items = [item for item in self.items if item["name"] != name]
            self.total_price -= price
        elif name not in [item["name"] for item in self.items]:
            self.items.append(
                {"name": name, "price": price, "id": id, "category": category}
            )
            self.total_price += price
            self.toggle_checked(name)

    @rx.event
    def delete(self):
        self.items = []
        self.total_price = 0
        self.is_checked = {checkbox_name: False for checkbox_name in self.all_checked}
