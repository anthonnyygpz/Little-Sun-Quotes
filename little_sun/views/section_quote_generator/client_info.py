import reflex as rx

from little_sun.components.labels import create_heading

from .components.buttons import switch_selection
from .components.forms import form_client_input, form_client_switch


def client_information_section(state_clients):
    """Create the client information section of the form."""
    return rx.box(
        create_heading(text="Informacion del cliente"),
        rx.cond(
            state_clients.is_exists,
            form_client_switch(state_clients=state_clients),
            form_client_input(state_clients=state_clients),
        ),
        switch_selection(state_clients=state_clients),
        on_mount=state_clients.reset_all,
        bacspaceround_color="#ffffff",
        margin_bottom="2rem",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )


def client_update_section(state_clients):
    return rx.box(
        create_heading(text="Informacion del cliente"),
        form_client_input(state_clients=state_clients),
        on_mount=state_clients.reset_all,
        bacspaceround_color="#ffffff",
        margin_bottom="2rem",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )
