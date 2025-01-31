import reflex as rx
from little_sun.repositories.info_client import ClientsState


def select():
    return rx.cond(
        ClientsState.error,
        rx.text(ClientsState.error, color_scheme="red"),
        rx.select.root(
            rx.select.trigger(placeholer="No Seleccionado"),
            rx.select.content(
                rx.select.group(
                    rx.foreach(
                        ClientsState.data,
                        lambda item: rx.select.item(
                            f"{item.name}",
                            value=f"{item.name}",
                        ),
                    ),
                ),
            ),
            value=f"{ClientsState.name_client}",
            on_change=ClientsState.update_name,  # type: ignore
        ),
    )
