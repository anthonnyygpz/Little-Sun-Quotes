import httpx


class QuotesAPINotUseRx:
    async def post_data(self, parameter):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    "http://0.0.0.0:8000/api/create_quotes",
                    json=parameter,
                )
                response.raise_for_status()
                return response.json()
        except Exception as e:
            print(f"Error fetching data: {str(e)}")

    # async def one_fetch_data(self, name):
    #     try:
    #         async with httpx.AsyncClient() as client:
    #             response = await client.get(
    #                 f"http://0.0.0.0:8000/api/get_one_clients?name={name}",
    #             )
    #             response.raise_for_status()
    #             return response.json()
    #     except Exception as e:
    #         print(f"Error fetching data: {str(e)}")
