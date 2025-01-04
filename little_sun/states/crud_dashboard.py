from typing import Dict, List
import reflex as rx

from little_sun.states.api_client import APIClient


class CRUDDashboard(rx.State):
    user: List[Dict] = []

    async def get_quotes(self):
        return await APIClient().get_data(endpoint="get_quotes_data")

    @rx.event(background=True)
    async def view_quotes(self):
        async with self:
            item = await self.get_quotes()
            if item == None:
                return
            self.user = item  # type: ignore

    async def post_data(self):
        pass

    async def delete_data(self, id: int):
        return await APIClient().delete_data(
            endpoint=f"delete_quote?quote_id={id}"
        )

    @rx.event
    async def update_quotes(self, form_data: dict):
        print(form_data)

    @rx.event
    async def delete_quotes(self, quote_id):
        message = await self.delete_data(id=quote_id)
