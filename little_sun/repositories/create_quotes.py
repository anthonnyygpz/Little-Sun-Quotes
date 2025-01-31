import logging
from typing import Dict, Optional

import httpx
import reflex as rx
from pydantic import BaseModel, ValidationError

logger = logging.getLogger(__name__)


class QuotesModel(BaseModel):
    client_id: Optional[int]
    nail_size_id: Optional[int]
    total_amount: Optional[int]


class ClientCreate(BaseModel):
    name: Optional[str]
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
            try:
                response = await client.get(
                    f"http://0.0.0.0:8000/api_v1/clients/?name_in={name}"
                )
                response.raise_for_status()
                return response.json()
            except Exception:
                return

    async def register_client(self, post_client: ClientCreate):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://0.0.0.0:8000/api_v1/clients/",
                json=post_client.model_dump(),
            )
            response.raise_for_status()
            return response.json()

    async def get_name_clients(self, name: str, phone_number: str = ""):
        try:
            get_name_client = await self.get_client_exist(name)
            print(get_name_client)
            if get_name_client:
                self.client_id = get_name_client["client_id"]
                return get_name_client
            else:
                new_client_model = ClientCreate(name=name, phone_number=phone_number)
                register_client = await self.register_client(
                    post_client=new_client_model
                )
                self.client_id = register_client["client_id"]
                return register_client
        except httpx.HTTPError as he:
            logger.error(f"HTTP error occurred: {he}")
        except Exception as e:
            logger.error(f"An error occurred: {e}")
        return None

    async def create_quote(self, quote: QuotesModel):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://0.0.0.0:8000/api_v1/quotes/create", json=quote.model_dump()
            )
            response.raise_for_status()
            self.id_quote = response.json()["quote_id"]
            return response.json()

    async def create_quote_services(self, quote_service: QuoteServicesCreate):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://0.0.0.0:8000/api_v1/quote_services/",
                json=quote_service.model_dump(),
            )
            response.raise_for_status()
            return response.json()

    async def create_quote_design(self, quote_design: QuoteDesignsCreate):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://0.0.0.0:8000/api_v1/quote_designs/",
                json=quote_design.model_dump(),
            )
            response.raise_for_status()
            return response.json()

    async def update_form_data(self, form_data: Dict):
        try:
            name = form_data.get("name")
            phone_number = form_data.get("phone_number", 0)
            if not name:
                raise ValueError("Name is required in form data")

            await self.get_name_clients(name, phone_number)

            nail_size_id = form_data.get("nail_size_id")
            total_price_service = form_data.get("total_price_service", 0)
            total_price_design = form_data.get("total_price_design", 0)

            if not all([nail_size_id, total_price_service, total_price_design]):
                raise ValueError("Missing required fields in form data")

            await self.create_quote(
                QuotesModel(
                    client_id=self.client_id,
                    nail_size_id=nail_size_id,
                    total_amount=total_price_service + total_price_design,
                )
            )

            services = form_data.get("services", [])
            for item in services:
                await self.create_quote_services(
                    QuoteServicesCreate(quote_id=self.id_quote, service_id=item["id"])
                )

            designs = form_data.get("designs", [])
            for item in designs:
                await self.create_quote_design(
                    QuoteDesignsCreate(quote_id=self.id_quote, design_id=item["id"])
                )

            yield rx.redirect("http://localhost:3000/")
        except httpx.HTTPError as he:
            logger.error(f"HTTP error occurred: {he}")
        except ValidationError as ve:
            logger.error(f"Validation error occurred: {ve}")
        except Exception as e:
            logger.error(f"An error occurred: {e}")
