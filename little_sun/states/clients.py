from typing import List, Dict
import httpx
import reflex as rx


class ClientsAPI(rx.State):
    data: List[Dict] = []
    error: str = ""
    loading: bool = False

    async def fetch_data(self):
        self.loading = True
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    "http://0.0.0.0:8000/api/get_clients",
                )
                response.raise_for_status()
                self.data = response.json()
        except Exception as e:
            self.error = f"Error fetching data: {str(e)}"
        finally:
            self.loading = False

    # async def one_fetch_data(self, parameter):
    #     self.loading = True
    #     try:
    #         async with httpx.AsyncClient() as client:
    #             response = await client.post(
    #                 "http://0.0.0.0:8000/api/get_one_clients",
    #                 json=parameter,
    #             )
    #             response.raise_for_status()
    #             self.data = response.json()
    #     except Exception as e:
    #         self.error = f"Error fetching data: {str(e)}"
    #     finally:
    #         self.loading = False


class ClientsAPINotUseRx:
    async def post_data(self, parameter):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    "http://0.0.0.0:8000/api/register_clients",
                    json=parameter,
                )
                response.raise_for_status()
                return response.json()
        except Exception as e:
            print(f"Error fetching data: {str(e)}")

    async def one_fetch_data(self, name):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"http://0.0.0.0:8000/api/get_one_clients?name={name}",
                )
                response.raise_for_status()
                return response.json()
        except Exception as e:
            print(f"Error fetching data: {str(e)}")
