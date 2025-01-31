import reflex as rx

from little_sun.components.forms import create_checkbox
from little_sun.components.pricing import create_price_span
from little_sun.components.section_banner import section_banner
from little_sun.repositories.designs import DesignsState


def design():
    return section_banner(
        state_var=DesignsState,
        label_text="Selecciona un diseño",
        content=rx.box(
            rx.foreach(
                DesignsState.data,
                lambda item: rx.flex(
                    create_checkbox(
                        checkbox_id=f"{item.design_id}",
                        checkbox_name=f"{item.design_name}",
                        price=item.price,
                        state=DesignsState,
                    ),
                    create_price_span(price_text=f"${item.price}"),
                    display="flex",
                    align_items="center",
                ),
            ),
            on_mount=[DesignsState.all_designs, DesignsState.reset_all],
            display="flex",
            flex_direction="column",
            gap="0.5rem",
        ),
    )
