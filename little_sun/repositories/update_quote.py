import httpx
from pydantic import BaseModel
import reflex as rx
from typing import Dict, List


class UpdateQuoteModel(BaseModel):
    quote_id: int
    client_id: int
    name: str
    phone_number: int
    nail_size_id: int
    total_amount: int
    status: str
    designs: List
    services: List


class UpdateQuote(rx.State):
    pass

    async def update_quotes(self, form_data: UpdateQuoteModel):
        async with httpx.AsyncClient() as client:
            response = await client.put(
                "http://0.0.0.0:8000/api/update_quotes", json=form_data.model_dump()
            )
            response.raise_for_status()
            response.json()
            print(response.json())

    @rx.event
    async def update_form_data(self, form_data: Dict):
        services = []
        designs = []
        for item in form_data["service"]:
            services.append(item["id"])

        for item in form_data["design"]:
            designs.append(item["id"])

        form_data["service"] = services
        form_data["design"] = designs

        await self.update_quotes(
            UpdateQuoteModel(
                quote_id=form_data["quote_id"],
                client_id=form_data["client_id"],
                name=form_data["name_client"],
                phone_number=form_data["phone_number"],
                nail_size_id=form_data["size_id"],
                total_amount=form_data["total_price"],
                status=form_data["status"],
                designs=form_data["design"],
                services=form_data["service"],
            )
        )
