from __future__ import print_function
from typing import Dict, List

from pydantic import BaseModel
import reflex as rx

from little_sun.services.api_clients import DataFetcher, DataFetchError, logger


class QuoteUpdate(BaseModel):
    quote_id: int
    client_id: int
    name: str
    nail_size_id: int
    services: List[int]
    designs: List[int]
    total_amount: int
    status: str


class QuoteAPI:
    def __init__(self, base_url: str = "http://0.0.0.0:8000"):
        self.fetcher = DataFetcher(base_url, cache_ttl=1800)
        self.list_endpoint = "/api/get_quotes_data"
        self.delete_endpoint = "/api/delete_quote"

    async def get_quotes(self) -> List[Dict]:
        async with self.fetcher as fetcher:
            response = await fetcher.fetch_data(self.list_endpoint)
            return response.data  # type: ignore

    async def update_quotes(self, quote: QuoteUpdate) -> Dict:
        async with self.fetcher as fetcher:
            response = await fetcher.fetch_data(
                "/api/update_quotes",
                method="PUT",
                data=quote.model_dump(),
                use_cache=True,
            )
            return response.data  # type:ignore

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
    form_data: Dict = {}

    @rx.event(background=True)
    async def view_quotes(self):
        quotes_api = QuoteAPI()
        async with self:
            try:
                logger.info("Fetching user 1 (second time)...")
                quotes = await quotes_api.get_quotes()
                if quotes == []:
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

    async def update_quotes(self, form_data):
        quotes_api = QuoteAPI()
        try:
            update_quote = QuoteUpdate(
                quote_id=form_data["quote_id"],
                client_id=form_data["client_id"],
                name=form_data["name_client"],
                nail_size_id=form_data["size"],
                services=form_data["services"],
                designs=form_data["designs"],
                total_amount=form_data["total_price"],
                status=form_data["status"],
            )
            update = await quotes_api.update_quotes(quote=update_quote)
            return update
        except DataFetchError as e:
            print(str(e))

    @rx.event
    async def update_form_data(self, form_data: Dict):
        services = []
        designs = []
        for i in form_data["service"]:
            if i["category"] == "design":
                designs.append(i["id"])

            if i["category"] == "service":
                services.append(i["id"])

        form_data.pop("service")
        form_data["services"] = services
        form_data["designs"] = designs

        print(form_data)
        await self.update_quotes(form_data)

        # self.form_data = {}
        # form_data_cleaned = form_data.copy()
        # services = []
        # designs = []
        # keys_to_remove = []
        #
        # for key, value in form_data.items():
        #     if key.startswith("service_") and value:
        #         service_id = key.replace("service_", "")
        #         services.append(service_id)
        #         keys_to_remove.append(key)
        #     elif key.startswith("design_") and value:
        #         design_id = key.replace("design_", "")
        #         designs.append(design_id)
        #         keys_to_remove.append(key)
        #
        # for key in keys_to_remove:
        #     del form_data_cleaned[key]
        #
        # self.form_data = form_data_cleaned
        # self.form_data["service"] = services
        # self.form_data["designs"] = designs
        # print(self.form_data)

        # await self.update_quote()
