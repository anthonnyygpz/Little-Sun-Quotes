from typing import Dict, List
import httpx
import reflex as rx


class NailSizesState(rx.State):
    size_id: int = 0
    type_escultural: str = ""
    name_size: str = ""
    is_loading: bool = False

    data: List[Dict]
    error: str = ""

    def reset_all(self):
        self.size_id = 0
        self.type_escultural = ""
        self.name_size = ""
        self.is_loading = False
        self.error = ""

    async def all_nail_sizes(self):
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(
                    "http://0.0.0.0:8000/api_v1/sculpign_nail_size/"
                )
                response.raise_for_status()
                self.data = response.json()
            except Exception:
                self.error = "El recurso solicitado no se encontró"

    @rx.event
    def update_type_escultural(self, type_escultural: str):
        self.type_escultural = type_escultural

    @rx.event
    def update_size_id(self, size_id: int):
        self.size_id = size_id
