from typing import Dict, List
import reflex as rx
import httpx


class CheckboxState(rx.State):
    items: List[Dict] = []
    total_price: int = 0
    type_escultural: str = ""
    form_quote: dict = {"nail_size": 0, "service": [], "design": []}
    service_list: list = []
    is_disabled: bool = False
    value_texts: dict = {}

    def on_load(self):
        self.items = []
        self.total_price = 0
        self.type_escultural = ""
        self.is_disabled = False
        self.form_quote = {}

    async def register_client(self, parameter):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    "http://0.0.0.0:8000/api/register_clients", json=parameter
                )
                response.raise_for_status()
                print(response.json())
        except Exception as e:
            self.error = f"Error fetching data: {str(e)}"
        # finally:
        #     self.loading = False

    async def upload_data_budget(self, data_to_send):
        # self.loading = True
        # data_to_send.json()

        print(data_to_send)
        # try:
        #     async with httpx.AsyncClient() as client:
        #         response = await client.post(
        #             "http://0.0.0.0:8000/api/upload_budgets", json=data_to_send
        #         )
        #         response.raise_for_status()
        #         print(response.json())
        # except Exception as e:
        #     self.error = f"Error fetching data: {str(e)}"
        # finally:
        #     self.loading = False

    @rx.event
    async def upload(self):
        # self.form_quote = {
        #     "nail_size": self.type_escultural,
        #     "service": [],
        #     "design": [],
        # }

        for item in self.items:
            if item["category"] == "service":
                self.form_quote["service"].append(item["id"])
            elif item["category"] == "design":
                self.form_quote["design"].append(item["id"])
        await self.upload_data_budget(self.form_quote)

    @rx.event
    def add_type_escultural(self, item):
        self.type_escultural = item["type_escultural"]
        self.form_quote["nail_size"] = item["nail_size_id"]

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

    @rx.event
    def delete_all(self):
        """Reinicia todos los checkboxes y el precio total"""
        self.items = []
        self.total_price = 0
        self.type_escultural = ""
        self.form_quote = {}
