from typing import Dict, List
import reflex as rx

from little_sun.states.clients import ClientsAPINotUseRx


class State(rx.State):
    form_data: Dict = {}
    form_data_client: List[Dict] = []

    async def register_clients(
        self, name_client: str, phone_number: str = None  # type: ignore
    ):
        json = {"name": name_client, "phone_number": phone_number}
        await ClientsAPINotUseRx().post_data(parameter=json)

    async def get_name_client(self, name: str, phone_number: str = None):  # type: ignore
        get_data = await ClientsAPINotUseRx().one_fetch_data(name)
        if get_data:
            return get_data
        else:
            return await self.register_clients(name, phone_number)

    @rx.event
    async def upload_data(self, item: Dict):
        # item_data = await self.get_name_client(
        #     item["name_client"], item["phone_number"]
        # )
        x = [i["id"] for i in item["service"]]
        rx.console_log("ohla")
        print(x)
