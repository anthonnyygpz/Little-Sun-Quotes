from typing import Dict, List, Optional

import httpx
import reflex as rx
from pydantic import BaseModel


class QuotesModel(BaseModel):
    client_id: int
    nail_size_id: int
    total_amount: int


class ClientCreate(BaseModel):
    name: str
    phone_number: Optional[int]


class QuoteServicesCreate(BaseModel):
    quote_id: int
    service_id: int


class QuoteDesignsCreate(BaseModel):
    quote_id: int
    design_id: int


class CreateQuotes(rx.State):
    client_id: int = 0
    id_quote: int = 0

    def reset_all(self):
        self.client_id = 0

    async def get_client_exist(self, name: str):
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"http://0.0.0.0:8000/api/get_one_clients?name={name}"
            )
            response.raise_for_status()
            return response.json()

    async def register_client(self, post_client: ClientCreate):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://0.0.0.0:8000/api/register_clients",
                json=post_client.model_dump(),
            )
            response.raise_for_status()
            return response.json()

    async def get_name_clients(self, name: str, phone_number: int = 0):
        try:
            get_name_client = await self.get_client_exist(name)
            if get_name_client:
                self.client_id = get_name_client[0]["client_id"]
                return get_name_client
            else:
                new_client_model = ClientCreate(name=name, phone_number=phone_number)
                register_client = await self.register_client(
                    post_client=new_client_model
                )
                self.client_id = register_client["client_id"]

                return register_client
        except httpx.HTTPError as he:
            print(str(he))
        except Exception as e:
            print(str(e))

    async def create_quote(self, quote: QuotesModel):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://0.0.0.0:8000/api/create_quotes", json=quote.model_dump()
            )
            response.raise_for_status()
            self.id_quote = response.json()["quote_id"]
            return response.json()

    async def create_quote_services(self, quote_service: QuoteServicesCreate):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://0.0.0.0:8000/api/create_quote_services",
                json=quote_service.model_dump(),
            )
            response.raise_for_status()
            return response.json()

    async def create_quote_design(self, quote_design: QuoteDesignsCreate):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://0.0.0.0:8000/api/create_quote_designs",
                json=quote_design.model_dump(),
            )
            response.raise_for_status()
            return response.json()

    async def update_form_data(self, form_data: Dict):
        await self.get_name_clients(form_data["name_client"], form_data["phone_number"])
        await self.create_quote(
            QuotesModel(
                client_id=self.client_id,
                nail_size_id=form_data["size_id"],
                total_amount=form_data["total_price_service"]
                + form_data["total_price_design"],
            )
        )
        for item in form_data["service"]:
            await self.create_quote_services(
                QuoteServicesCreate(quote_id=self.id_quote, service_id=item["id"])
            )

        for item in form_data["design"]:
            await self.create_quote_design(
                QuoteDesignsCreate(quote_id=self.id_quote, design_id=item["id"])
            )
