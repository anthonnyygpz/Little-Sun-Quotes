import reflex as rx

from little_sun.repositories.info_client import InfoClient


from ...components.labels import create_heading
from .components.forms import form_client_switch, form_client_input
from .components.buttons import switch_selection
from ...states.state import State


def client_information_section():
    """Create the client information section of the form."""
    return rx.box(
        create_heading(text="Informacion del cliente"),
        rx.cond(
            InfoClient.is_exists,
            form_client_switch(),
            form_client_input(),
        ),
        switch_selection(),
        on_mount=State.get_method,
        bacspaceround_color="#ffffff",
        margin_bottom="2rem",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )


def client_update_section():
    return rx.box(
        create_heading(text="Informacion del cliente"),
        form_client_input(),
        on_mount=State.get_method,
        bacspaceround_color="#ffffff",
        margin_bottom="2rem",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )
