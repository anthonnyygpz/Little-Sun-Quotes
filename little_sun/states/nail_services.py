from typing import Dict, List
import reflex as rx
import httpx


class NailServicesAPI(rx.State):
    data: List[Dict] = []
    error: str = ""
    loading: bool = False

    async def fetch_data(self):
        self.loading = True
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    "http://0.0.0.0:8000/api/get_nail_services"
                )
                response.raise_for_status()
                self.data = response.json()
        except Exception as e:
            self.error = f"Error fetching data: {str(e)}"
        finally:
            self.loading = False


class NailServices(rx.State):
    items: List[Dict] = []
    total_price: int = 0
    all_checked: List = []
    is_checked: dict[str, bool] = {
        checkbox_name: False for checkbox_name in all_checked
    }

    def on_mount(self):
        self.items = []
        self.total_price = 0
        self.is_checked = {
            checkbox_name: False for checkbox_name in self.all_checked
        }

    def toggle_checked(self, checkbox_name: str) -> None:
        self.all_checked = [item["name"] for item in self.items]

        if checkbox_name not in self.is_checked:
            self.is_checked[checkbox_name] = False

        self.is_checked[checkbox_name] = not self.is_checked.get(
            checkbox_name, False
        )

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
        self.is_checked = {
            checkbox_name: False for checkbox_name in self.all_checked
        }
