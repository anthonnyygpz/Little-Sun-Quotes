import reflex as rx

from little_sun.repositories.designs import DesignsState


def create_price_span(price_text):
    """Create a span element for displaying prices."""
    return rx.text.span(
        price_text,
        class_name="ml-auto",
        font_weight="500",
        color="#111827",
        font_size="0.875rem",
        line_height="1.25rem",
    )


def create_price_row(label_text, price, color=None, font_weight=None):
    """Create a row displaying a price label and amount."""
    return rx.text(
        rx.text.span(label_text),
        rx.text.span(f"${price}"),
        display="flex",
        justify_content="space-between",
        font_weight=font_weight,
        color_scheme=color,
    )
