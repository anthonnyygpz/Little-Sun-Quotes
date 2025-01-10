import reflex as rx


from little_sun.utils.constants import Colors
from ...components.forms import create_checkbox
from ...components.labels import create_heading
from ...components.pricing import create_price_span


def designs_selection_section(state_designs, label_text):
    """Create the services selection section of the form."""
    return rx.box(
        create_heading(label_text),
        rx.box(
            rx.cond(
                state_designs.loading,
                rx.spinner(),
                rx.cond(
                    state_designs.error != "",
                    rx.text(state_designs.error, color=Colors.error),
                    rx.foreach(
                        state_designs.data,
                        lambda item: rx.flex(
                            create_checkbox(
                                checkbox_id=f"{item.design_id}",
                                checkbox_name=f"{item.design_name}",
                                price=item.price,
                                category="design",
                            ),
                            create_price_span(price_text=f"${item.price}"),
                            display="flex",
                            align_items="center",
                        ),
                    ),
                ),
            ),
            on_mount=[state_designs.fetch_data],
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
