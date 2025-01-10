from typing import Dict, List
import reflex as rx
from little_sun.services.api_clients import logger, DataFetchError, DataFetcher


class NailSizesAPI:
    def __init__(self, base_url: str = "http://0.0.0.0:8000"):
        self.fetcher = DataFetcher(base_url, cache_ttl=1800)
        self.list_endpoint = "/api/get_nail_sizes"

    async def get_nail_sizes(self) -> List[Dict]:
        async with self.fetcher as fetcher:
            response = await fetcher.fetch_data(self.list_endpoint)
            return response.data  # type: ignore


class NailSizesState(rx.State):
    data: List[Dict] = []
    error: str = ""
    loading: bool = False

    type_escultural: str = ""
    id_type_escultural: int = 0

    async def fetch_data(self):
        self.loading = True
        api = NailSizesAPI()
        try:
            logger.info("Fetching user 1 (second time)...")
            nail_sizes = await api.get_nail_sizes()
            self.data = nail_sizes
        except DataFetchError as he:
            self.error = f"Error fetching data: {str(he)}"
        except Exception as e:
            self.error = f"Error fetching data: {str(e)}"
        finally:
            self.loading = False

    def on_mount(self):
        self.type_escultural = ""

    @rx.event
    def add_type_escultural(self, item):
        self.type_escultural = item["size_name"]
        self.id_type_escultural = item["size_id"]

    @rx.event
    def delete(self):
        self.type_escultural = ""
