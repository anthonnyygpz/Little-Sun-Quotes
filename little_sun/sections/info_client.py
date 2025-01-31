import reflex as rx

from little_sun.components.form import form
from little_sun.components.forms import input_text
from little_sun.components.labels import heading, label
from little_sun.components.select import select
from little_sun.components.switch import switch
from little_sun.repositories.info_client import ClientsState
from little_sun.repositories.params_url import ParamsUrl


def info_client():
    return rx.match(
        ParamsUrl.params_data["method"],
        (
            "POST",
            rx.box(
                heading(text="Informacion del cliente"),
                rx.cond(
                    ClientsState.is_exists,
                    form(
                        state_var=ClientsState,
                        content=rx.box(
                            label(label_text="Nombre del cliente"),
                            select(),
                        ),
                    ),
                    form(
                        state_var=ClientsState,
                        content=rx.box(
                            rx.box(
                                label(label_text="Nombre del cliente"),
                                input_text(
                                    input_id="clientName",
                                    input_name="clientName",
                                    input_type="text",
                                    on_blur=ClientsState.update_name,  # type: ignore
                                    text_value=ClientsState.name_client,
                                ),
                            ),
                            rx.box(
                                label(label_text="Numero de telefono (Opcional)"),
                                input_text(
                                    input_id="clientNumber",
                                    input_name="clientNumber",
                                    input_type="text",
                                    on_blur=ClientsState.update_phone_number,  # type: ignore
                                    text_value=ClientsState.phone_number,
                                ),
                            ),
                        ),
                    ),
                ),
                switch(),
                on_mount=ClientsState.reset_all,
                bacspaceround_color="#ffffff",
                margin_bottom="2rem",
                padding="1.5rem",
                border_radius="0.5rem",
                box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
            ),
        ),
        (
            "PUT",
            rx.box(
                heading(text="Informacion del cliente"),
                form(
                    state_var=ClientsState,
                    content=rx.box(
                        rx.box(
                            label(label_text="Nombre del cliente"),
                            input_text(
                                input_id="clientName",
                                input_name="clientName",
                                input_type="text",
                                on_blur=ClientsState.update_name,  # type: ignore
                                text_value=ClientsState.name_client,
                            ),
                        ),
                        rx.box(
                            label(label_text="Numero de telefono (Opcional)"),
                            input_text(
                                input_id="clientNumber",
                                input_name="clientNumber",
                                input_type="text",
                                on_blur=ClientsState.update_phone_number,  # type: ignore
                                text_value=ClientsState.phone_number,
                            ),
                        ),
                    ),
                ),
                on_mount=ClientsState.reset_all,
                bacspaceround_color="#ffffff",
                margin_bottom="2rem",
                padding="1.5rem",
                border_radius="0.5rem",
                box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
            ),
        ),
    )
