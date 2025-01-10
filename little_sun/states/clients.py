from typing import List, Dict, Optional
from pydantic import BaseModel
import reflex as rx
from little_sun.services.api_clients import logger, DataFetchError, DataFetcher


class ClientCreate(BaseModel):
    name: str
    phone_number: Optional[int]


class ClientsApi:
    def __init__(self, base_url: str = "http://0.0.0.0:8000"):
        self.fetcher = DataFetcher(base_url, cache_ttl=1800)
        self.list_endpoint = "/api/get_clients"

    async def get_all(self) -> List[Dict]:
        async with self.fetcher as fetcher:
            response = await fetcher.fetch_data(self.list_endpoint)
            return response.data  # type: ignore

    async def get_client_by_name(self, name: str) -> Dict:
        async with self.fetcher as fetcher:
            params = {"name": name}
            response = await fetcher.fetch_data("/api/get_one_clients", params=params)
            return response.data  # type: ignore

    async def create(self, client: ClientCreate) -> Dict:
        async with self.fetcher as fetcher:
            response = await fetcher.fetch_data(
                "/api/register_clients",
                method="POST",
                data=client.model_dump(),
                use_cache=False,
            )
            return response.data  # type: ignore


class ClientsState(rx.State):
    name_client: str = ""
    phone_number: int = 0
    register_or_exist: bool = False

    data: List[Dict] = []
    error: str = ""
    loading: bool = False

    async def fetch_data(self):
        api = ClientsApi()
        self.loading = True
        try:
            logger.info("Fetching user 1 (second time)...")
            clients = await api.get_all()
            self.data = clients
        except DataFetchError as he:
            self.error = f"{str(he)}"
        except Exception as e:
            self.error = f"Error fetching data: {str(e)}"
        finally:
            self.loading = False

    async def one_fetch_data(self, name: str):
        try:
            api = ClientsApi()
            clients = await api.get_client_by_name(name)
            return clients
        except DataFetchError as he:
            self.error = f"{str(he)}"
        except Exception as e:
            print(f"Error fetching data: {str(e)}")

    def on_mount(self):
        self.name_client = ""
        self.phone_number = 0
        self.register_or_exist = False

    def switch(self):
        self.name_client = ""
        self.phone_number = 0

    @rx.event
    def change_cheked(self, is_checked: bool):
        self.register_or_exist = is_checked
