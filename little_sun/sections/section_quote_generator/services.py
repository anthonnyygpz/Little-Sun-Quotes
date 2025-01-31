import reflex as rx
from little_sun.components.labels import heading
from little_sun.components.forms import create_checkbox
from little_sun.components.pricing import create_price_span


def services_selection_section(state_var, label_text):
    """Create the services selection section of the form."""
    return
    rx.box(
        heading(label_text),
        rx.cond(
            state_var.error,
            rx.text(state_var.error, color_scheme="red"),
            rx.box(
                rx.foreach(
                    state_var.data,
                    lambda item: rx.flex(
                        create_checkbox(
                            checkbox_id=f"{item.service_id}",
                            checkbox_name=f"{item.service_name}",
                            price=item.price,
                            state=state_var,
                        ),
                        create_price_span(price_text=f"${item.price}"),
                        display="flex",
                        align_items="center",
                    ),
                ),
                on_mount=[state_var.all_services, state_var.reset_all],
                display="flex",
                flex_direction="column",
                gap="0.5rem",
            ),
        ),
        background_color="#ffffff",
        margin_bottom="2rem",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )
