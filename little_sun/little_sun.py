import reflex as rx
from fastapi.middleware.cors import CORSMiddleware

from little_sun.backend.app.api.v1.endpoints import (
    clients,
    designs,
    quote_designs,
    quote_services,
    quotes,
    sculping_nail_sizes,
    services,
)
from little_sun.backend.app.db.session import settings
from little_sun.pages.dashboard import dashboard
from little_sun.pages.quote_generator import quote_generator

# Initalization
app = rx.App(
    theme=rx.theme(
        appearance="dark",
        has_background=True,
        radius="large",
        accent_color="grass",
    )
)

app.api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# APIs
app.api.title = settings.PROJECT_NAME
api_version = settings.API_VERSION_STR
app.api.include_router(
    services.router, prefix=f"{api_version}/services", tags=["Services"]
)
app.api.include_router(
    designs.router, prefix=f"{api_version}/designs", tags=["Designs"]
)
app.api.include_router(
    sculping_nail_sizes.router,
    prefix=f"{api_version}/sculpign_nail_size",
    tags=["Sculping_Nail_Size"],
)
app.api.include_router(
    clients.router, prefix=f"{api_version}/clients", tags=["Clients"]
)
app.api.include_router(quotes.router, prefix=f"{api_version}/quotes", tags=["Quotes"])
app.api.include_router(
    quote_designs.router, prefix=f"{api_version}/quote_designs", tags=["Quote_Designs"]
)
app.api.include_router(
    quote_services.router,
    prefix=f"{api_version}/quote_services",
    tags=["Quote_Services"],
)

# Routers reflex
app.add_page(quote_generator, route="/quote/[method]/[quote_id]/[id_client]")
app.add_page(dashboard, route="/")
# app.add_page(test, route="/test")

# from little_sun.pages.quote_generator import quote_generator
#
# from fastapi.middleware.cors import CORSMiddleware
# from .test.test import test
# from .pages.crud_dashboard import crud_dashboard
#
