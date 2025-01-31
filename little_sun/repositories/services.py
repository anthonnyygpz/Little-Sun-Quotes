from typing import Dict, List
import httpx
import reflex as rx


class ServicesState(rx.State):
    service_selected: List[Dict]
    selected: list[str]
    total_price: int

    data: List[Dict] = []
    error: str = ""
    all_checked: List = []
    is_checked: Dict[str, bool] = {
        checkbox_name: False for checkbox_name in all_checked
    }

    def reset_all(self):
        self.service_selected = []
        self.selected = []
        self.total_price = 0
        self.error = ""

    async def all_services(self):
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get("http://0.0.0.0:8000/api_v1/services/")
                response.raise_for_status()
                self.data = response.json()
            except Exception:
                self.error = "El recurso solicitado no se encontró"

    @rx.event
    def toggle_item(self, name: str, price: int, id: int):
        if name in [item["name"] for item in self.service_selected]:
            self.service_selected = [
                item for item in self.service_selected if item["name"] != name
            ]
            self.total_price -= price
        elif name not in [item["name"] for item in self.service_selected]:
            self.service_selected.append({"name": name, "price": price, "id": id})
            self.total_price += price
