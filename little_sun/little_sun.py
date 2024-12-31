"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from .backend.app.routers import (
    nail_services,
    designs,
    nail_sizes,
    budgets,
    clients,
    quotes,
    quote_designs,
)
from fastapi.middleware.cors import CORSMiddleware
from .pages.index import index
from .test.test import test

# Initalization
app = rx.App()

app.api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# APIs
app.api.include_router(nail_services.router)
app.api.include_router(designs.router)
app.api.include_router(nail_sizes.router)
app.api.include_router(budgets.router)
app.api.include_router(clients.router)
app.api.include_router(quotes.router)
app.api.include_router(quote_designs.router)

# Routers reflex
app.add_page(index, route="/")
app.add_page(test, route="/test")
