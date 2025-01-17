from typing import Dict, List
import httpx
import reflex as rx


class NailSizesState(rx.State):
    size_id: int = 0
    type_escultural: str = ""
    name_size: str = ""
    is_loading: bool = False

    data: List[Dict]

    async def all_nail_sizes(self):
        try:
            self.is_loading = True
            async with httpx.AsyncClient() as client:
                response = await client.get("http://0.0.0.0:8000/api/get_nail_sizes")
                response.raise_for_status()
                self.data = response.json()
        except Exception as e:
            print(str(e))
        finally:
            self.is_loading = False

    def reset_all(self):
        self.size_id = 0
        self.type_escultural = ""
        self.name_size = ""
        self.is_loading = False

    @rx.event
    def update_type_escultural(self, type_escultural: str):
        self.type_escultural = type_escultural

    @rx.event
    def update_size_id(self, size_id: int):
        self.size_id = size_id
