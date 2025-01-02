from typing import Dict
import reflex as rx

from little_sun.states.api_client import (
    QuoteServicesAPINoUseRx,
    QuoteDesignAPINoUseRx,
)
from little_sun.states.clients import ClientsAPINotUseRx
from little_sun.states.quotes import QuotesAPINotUseRx


class State(rx.State):
    client_id: int = 0
    quote_id: int = 0

    def on_mount(self):
        self.client_id = 0
        self.quote_id: int = 0

    async def register_clients(
        self, name_client: str, phone_number: str = None  # type: ignore
    ):
        json = {"name": name_client, "phone_number": phone_number}
        return await ClientsAPINotUseRx().post_data(parameter=json)

    async def get_name_client(self, name: str, phone_number: str = None):  # type: ignore
        get_data = await ClientsAPINotUseRx().one_fetch_data(name)
        if get_data:
            self.client_id = get_data[0]["client_id"]
            return get_data
        else:
            register_data = await self.register_clients(name, phone_number)
            self.client_id = register_data["client_id"]  # type: ignore
            return register_data

    async def create_quotes(
        self, client_id: int, nail_size_id: int, total_amount: int
    ):
        json = {
            "client_id": client_id,
            "nail_size_id": nail_size_id,
            "total_amount": total_amount,
        }

        quote_data = await QuotesAPINotUseRx().post_data(parameter=json)
        self.quote_id = quote_data["quote_id"]  # type: ignore
        return quote_data

    async def create_quote_service(self, service_id: int):
        json = {
            "quote_id": self.quote_id,
            "service_id": service_id,
        }
        quote_service_data = await QuoteServicesAPINoUseRx().post_data(
            endpoint="create_quote_services", parameter=json
        )
        return quote_service_data

    async def create_quote_design(self, design_id: int):
        json = {
            "quote_id": self.quote_id,
            "design_id": design_id,
        }
        return await QuoteDesignAPINoUseRx().post_data(parameter=json)

    @rx.event
    async def upload_data(self, item: Dict):
        """Upload data in dabase"""
        # create or get client
        await self.get_name_client(item["name_client"], item["phone_number"])

        await self.create_quotes(
            self.client_id, item["size"], item["total_price"]
        )
        for i in item["service"]:
            if i["category"] == "design":
                await self.create_quote_design(i["id"])
            if i["category"] == "service":
                pass
                await self.create_quote_service(i["id"])
