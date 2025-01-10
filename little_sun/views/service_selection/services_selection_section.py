import reflex as rx

from ...components.pricing import create_price_span

from ...components.forms import create_checkbox
from ...components.labels import create_heading
from ...utils.constants import Colors


def services_selection_section(state_services, label_text):
    """Create the services selection section of the form."""
    return rx.box(
        create_heading(label_text),
        rx.box(
            rx.cond(
                state_services.loading,
                rx.spinner(),
                rx.cond(
                    state_services.error != "",
                    rx.text(state_services.error, color=Colors.error),
                    rx.foreach(
                        state_services.data,
                        lambda item: rx.flex(
                            create_checkbox(
                                checkbox_id=f"{item.service_id}",
                                checkbox_name=f"{item.service_name}",
                                price=item.price,
                                category="service",
                            ),
                            create_price_span(price_text=f"${item.price}"),
                            display="flex",
                            align_items="center",
                        ),
                    ),
                ),
            ),
            on_mount=[state_services.fetch_data],
            display="flex",
            flex_direction="column",
            gap="0.5rem",
        ),
        background_color="#ffffff",
        margin_bottom="2rem",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )
