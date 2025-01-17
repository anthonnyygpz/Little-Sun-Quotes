import reflex as rx
from little_sun.utils.constants import Colors


def add_client_button() -> rx.Component:
    return rx.button(
        rx.icon("plus", size=26),
        rx.text("Agregar cliente", size="4", display=["none", "none", "block"]),
        bg=Colors.purple,
        size="3",
    )
