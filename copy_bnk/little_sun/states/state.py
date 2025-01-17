from typing import Dict
import reflex as rx

from little_sun.states.clients import ClientCreate, ClientsApi
from little_sun.states.quotes import QuotesApi, CreateQuotes
from little_sun.states.quote_services import QuoteServicesApi, QuoteServicesCreate
from little_sun.states.quote_designs import QuotDesignsApi, QuoteDesignsCreate


class State(rx.State):
    client_id: int = 0
    item_data: dict = {}

    def on_mount(self):
        self.client_id = 0
        self.quote_id: int = 0

    async def get_name_client_exist(self, name: str):
        api_clients = ClientsApi()
        return await api_clients.get_client_by_name(name)

    # Get name of client
    async def get_name_clients(self, name: str, phone_number: int = 0):
        api_clients = ClientsApi()
        try:
            get_name_client = await self.get_name_client_exist(name)
            if get_name_client:
                self.client_id = get_name_client[0]["client_id"]

                return get_name_client
            else:
                new_client_model = ClientCreate(name=name, phone_number=phone_number)
                register_client = await api_clients.create(client=new_client_model)
                self.client_id = register_client["client_id"]

                return register_client
        except Exception as e:
            print(str(e))

    async def create_quotes(self, client_id: int, nail_size_id: int, total_amount: int):
        api_quotes = QuotesApi()
        new_quotes_model = CreateQuotes(
            client_id=client_id,
            nail_size_id=nail_size_id,
            total_amount=total_amount,
        )
        create_quote = await api_quotes.create(quote=new_quotes_model)
        self.quote_id = create_quote["quote_id"]
        return create_quote

    async def create_quote_services(self, service_id: int):
        api_quote_service = QuoteServicesApi()
        create_quote_services_model = QuoteServicesCreate(
            quote_id=self.quote_id,
            service_id=service_id,
        )
        create_quote_service = await api_quote_service.create(
            quote_service=create_quote_services_model
        )
        return create_quote_service

    async def create_quote_design(self, design_id: int):
        api_quote_design = QuotDesignsApi()
        new_quote_design_model = QuoteDesignsCreate(
            quote_id=self.quote_id,
            design_id=design_id,
        )
        return await api_quote_design.create(quote_design=new_quote_design_model)

    @rx.event
    async def upload_data(self, item: Dict):
        await self.get_name_clients(item["name_client"], item["phone_number"])

        await self.create_quotes(self.client_id, item["size"], item["total_price"])

        for i in item["service"]:
            if i["category"] == "design":
                await self.create_quote_design(i["id"])
            if i["category"] == "service":
                await self.create_quote_services(i["id"])

    def get_method(self):
        params = self.router.page.params
        self.item_data = params
        # print(params)
