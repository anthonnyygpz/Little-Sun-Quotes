import reflex as rx


from ...components.labels import create_heading
from .components.forms import form_client_switch, form_client_input
from .components.buttons import switch_selection


def client_information_section(state_clients):
    """Create the client information section of the form."""
    return rx.box(
        create_heading(text="Informacion del cliente"),
        rx.cond(
            state_clients.register_or_exist,
            form_client_switch(state_clients=state_clients),
            form_client_input(state_clients=state_clients),
        ),
        switch_selection(state_clients=state_clients),
        bacspaceround_color="#ffffff",
        margin_bottom="2rem",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )
