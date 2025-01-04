import reflex as rx

from ....states.info_client import InfoClientState

from ....states.clients import ClientsAPI

from ....components.forms import create_input
from ....components.labels import create_label


def form_client_switch():
    return rx.form(
        rx.box(
            rx.box(
                create_label(label_text="Nombre del cliente"),
                rx.select.root(
                    rx.select.trigger(placeholder="No Seleccionado"),
                    rx.select.content(
                        rx.select.group(
                            rx.foreach(
                                ClientsAPI.data,
                                lambda item: rx.select.item(
                                    f"{item.name}",
                                    value=f"{item.name}",
                                ),
                            ),
                        ),
                    ),
                    value=f"{InfoClientState.name_client}",
                    on_change=InfoClientState.set_name_client,  # type: ignore
                ),
            ),
            gap="1rem",
            display="grid",
            grid_template_columns=rx.breakpoints(
                {
                    "0px": "repeat(1, minmax(0, 1fr))",
                    "768px": "repeat(2, minmax(0, 1fr))",
                }
            ),
            on_mount=lambda: [
                ClientsAPI.fetch_data,
            ],
        ),
    )


def form_client_input():
    return rx.form(
        rx.box(
            rx.box(
                create_label(label_text="Nombre del cliente"),
                create_input(
                    input_id="clientName",
                    input_name="clientName",
                    input_type="text",
                    on_blur=InfoClientState.set_name_client,  # type: ignore
                    text_value=InfoClientState.name_client,
                ),
            ),
            rx.box(
                create_label(label_text="Numero de telefono (Opcional)"),
                create_input(
                    input_id="clientNumber",
                    input_name="clientNumber",
                    input_type="text",
                    on_blur=InfoClientState.set_phone_number,  # type: ignore
                    text_value=InfoClientState.phone_number,
                ),
            ),
            on_mount=[InfoClientState.on_mount],
            gap="1rem",
            display="grid",
            grid_template_columns=rx.breakpoints(
                {
                    "0px": "repeat(1, minmax(0, 1fr))",
                    "768px": "repeat(2, minmax(0, 1fr))",
                }
            ),
        )
    )
