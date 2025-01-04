import reflex as rx

from ...states.info_client import InfoClientState

from ...components.labels import create_heading
from .components.forms import form_client_switch, form_client_input
from .components.buttons import switch_selection


def client_information_section():
    """Create the client information section of the form."""
    return rx.box(
        create_heading(text="Informacion del cliente"),
        rx.cond(
            InfoClientState.register_or_exist,
            form_client_switch(),
            form_client_input(),
        ),
        switch_selection(),
        bacspaceround_color="#ffffff",
        margin_bottom="2rem",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )
