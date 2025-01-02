from typing import Dict, List
import reflex as rx
import httpx


class NailSizesAPI(rx.State):
    data: List[Dict] = []
    error: str = ""
    loading: bool = False

    async def fetch_data(self):
        self.loading = True
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    "http://0.0.0.0:8000/api/get_nail_sizes"
                )
                response.raise_for_status()
                self.data = response.json()
        except Exception as e:
            self.error = f"Error fetching data: {str(e)}"
        finally:
            self.loading = False


class NailSizes(rx.State):
    type_escultural: str = ""
    id_type_escultural: int = 0

    def on_mount(self):
        self.type_escultural = ""

    @rx.event
    def add_type_escultural(self, item):
        self.type_escultural = item["size_name"]
        self.id_type_escultural = item["size_id"]

    @rx.event
    def delete(self):
        self.type_escultural = ""
