from typing import Dict, List
import httpx
import reflex as rx


class AllAppoiments(rx.State):
    data: List[Dict] = []

    async def all_appoiments(self):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get("http://0.0.0.0:8000/api_v1/quotes/all")
                response.raise_for_status()
                self.data = response.json()

        except httpx.HTTPError as e:
            print(f"Error HTTP: {e}")
            self.data = []
        except Exception as e:
            print(f"Error inesperado: {e}")
            self.data = []
