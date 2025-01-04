import reflex as rx

from little_sun.states.info_client import InfoClientState
from little_sun.states.nail_services import NailServices
from little_sun.states.nail_sizes import NailSizes


from ...components.labels import create_heading
from ...components.pricing import create_price_row

from ...states.state import State


def quote_summary_section():
    """Create the quote summary section."""
    return rx.box(
        create_heading(text="Resumen de la cita"),
        rx.box(
            create_heading(
                text=f"Nombre del cliente: {InfoClientState.name_client}"
            ),
            create_heading(
                text=f"Tipo de escultura usado: {NailSizes.type_escultural}"
            ),
            rx.foreach(
                NailServices.items,
                lambda item: create_price_row(
                    label_text=item.name, price=item.price, color="green"
                ),
            ),
            rx.divider(),
            create_price_row(
                label_text="Total:",
                price=NailServices.total_price,
                font_weight="600",
            ),
            # create_price_row(label_text="Tax (10%):", price=0.00),
            # rx.text(
            #     rx.text.span("Total:"),
            #     rx.text.span("$0.00"),
            #     display="flex",
            #     font_weight="600",
            #     justify_content="space-between",
            # ),
            on_mount=lambda: [
                NailSizes.on_mount,
                NailServices.on_mount,
                State.on_mount,
            ],
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
