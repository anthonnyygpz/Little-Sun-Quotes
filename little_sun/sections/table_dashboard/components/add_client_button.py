import reflex as rx


def add_client_button() -> rx.Component:
    return rx.button(
        rx.icon("plus", size=26),
        rx.text("Agregar cliente", size="4", display=["none", "none", "block"]),
        color_scheme="purple",
        size="3",
    )
