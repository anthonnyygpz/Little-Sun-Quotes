"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from .backend.app.routers import (
    services,
    designs,
    nail_sizes,
    budgets,
    clients,
    quotes,
    quote_designs,
    quote_services,
)
from fastapi.middleware.cors import CORSMiddleware
from .test.test import test
from .pages.index import index
from .pages.crud_dashboard import crud_dashboard

# Initalization
app = rx.App(
    theme=rx.theme(
        appearance="dark",
        has_background=True,
        radius="large",
        accent_color="grass",
    ),
)


app.api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# APIs
app.api.include_router(services.router)
app.api.include_router(designs.router)
app.api.include_router(nail_sizes.router)
app.api.include_router(budgets.router)
app.api.include_router(clients.router)
app.api.include_router(quotes.router)
app.api.include_router(quote_designs.router)
app.api.include_router(quote_services.router)

# Routers reflex
app.add_page(index, route="/quote")
app.add_page(crud_dashboard, route="/")
app.add_page(test, route="/test")
