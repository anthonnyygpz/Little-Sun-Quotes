import reflex as rx
from little_sun.components.labels import create_heading
from little_sun.components.forms import create_checkbox
from little_sun.components.pricing import create_price_span


def designs_selection_section(state_designs, label_text):
    """Create the services selection section of the form."""
    return rx.box(
        create_heading(label_text),
        rx.box(
            rx.foreach(
                state_designs.data,
                lambda item: rx.flex(
                    create_checkbox(
                        checkbox_id=f"{item.design_id}",
                        checkbox_name=f"{item.design_name}",
                        price=item.price,
                        state=state_designs,
                    ),
                    create_price_span(price_text=f"${item.price}"),
                    display="flex",
                    align_items="center",
                ),
            ),
            on_mount=[state_designs.all_designs, state_designs.reset_all],
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
