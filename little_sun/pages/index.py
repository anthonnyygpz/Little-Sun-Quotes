import reflex as rx
from ..templates.base import base_template
from ..views.quote_generator import quote_generator_view


def index() -> rx.Component:
    """Main page of the application."""
    return base_template(quote_generator_view())
