from typing import Dict, List
import reflex as rx
import httpx


class ClientsState(rx.State):
    name_client: str = ""
    phone_number: int = 0
    is_exists: bool = False

    data: List[Dict] = []

    async def all_client_info(self):
        async with httpx.AsyncClient() as client:
            response = await client.get("http://0.0.0.0:8000/api/get_clients")
            response.raise_for_status()
            self.data = response.json()

    def reset_all(self):
        self.name_client = ""
        self.phone_number = 0
        self.is_exists = False

    def reset_switch(self):
        self.name_client = ""
        self.phone_number = 0

    @rx.event
    def change_existence_status(self, status: bool):
        self.is_exists = status

    @rx.event
    def update_name(self, name: str) -> None:
        self.name_client = name

    def update_phone_number(self, phone_number: str):
        try:
            phone_num = int(phone_number)
            self.phone_number = phone_num
        except ValueError as e:
            print(str(e))
