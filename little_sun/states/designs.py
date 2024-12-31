from typing import Dict, List
import reflex as rx
import httpx


class DesignsAPI(rx.State):
    data: List[Dict] = []
    error: str = ""
    loading: bool = False

    async def fetch_data(self):
        self.loading = True
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    "http://0.0.0.0:8000/api/get_design"
                )
                response.raise_for_status()
                self.data = response.json()
        except Exception as e:
            self.error = f"Error fetching data: {str(e)}"
        finally:
            self.loading = False


class DesignsAPIPost:
    async def post_data(self, parameter):
        self.loading = True
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    "http://0.0.0.0:8000/api/register_clients",
                    json=parameter,
                )
                response.raise_for_status()
                self.data = response.json()
        except Exception as e:
            self.error = f"Error fetching data: {str(e)}"
        finally:
            self.loading = False
