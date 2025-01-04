import httpx


class QuoteServicesAPINoUseRx:
    async def post_data(self, endpoint, parameter):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"http://0.0.0.0:8000/api/{endpoint}",
                    json=parameter,
                )
                response.raise_for_status()
                return response.json()
        except Exception as e:
            print(f"Error fetching data: {str(e)}")


class QuoteDesignAPINoUseRx:
    async def post_data(self, parameter):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    "http://0.0.0.0:8000/api/create_quote_designs",
                    json=parameter,
                )
                response.raise_for_status()
                return response.json()
        except Exception as e:
            print(f"Error fetching data: {str(e)}")


class APIClient:
    async def post_data(self, endpoint, parameter):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"http://0.0.0.0:8000/api/{endpoint}",
                    json=parameter,
                )
                response.raise_for_status()
                return response.json()
        except Exception as e:
            print(f"Error fetching data: {str(e)}")

    async def get_data(self, endpoint):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"http://0.0.0.0:8000/api/{endpoint}",
                )
                response.raise_for_status()
                return response.json()
        except Exception as e:
            print(f"Error fetching data: {str(e)}")

    async def delete_data(self, endpoint):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.delete(
                    f"http://0.0.0.0:8000/api/{endpoint}",
                )
                response.raise_for_status()
                return response.json()
        except Exception as e:
            print(f"Error fetching data: {str(e)}")
