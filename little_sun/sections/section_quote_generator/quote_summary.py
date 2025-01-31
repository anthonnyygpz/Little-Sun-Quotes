import reflex as rx
from little_sun.components.labels import heading
from little_sun.components.pricing import create_price_row


def quote_summary_section(
    state_clients, state_nail_sizes, state_services, state_designs
):
    """Create the quote summary section."""
    return
    rx.box(
        heading(text="Resumen de la cita"),
        rx.box(
            heading(text=f"Nombre del cliente: {state_clients.name_client}"),
            heading(
                text=f"Tipo de escultura usado: {state_nail_sizes.type_escultural}"
            ),
            rx.foreach(
                state_services.service_selected,
                lambda item: create_price_row(
                    label_text=item.name, price=item.price, color="green"
                ),
            ),
            rx.foreach(
                state_designs.design_selected,
                lambda item: create_price_row(
                    label_text=item.name, price=item.price, color="green"
                ),
            ),
            rx.divider(),
            create_price_row(
                label_text="Total:",
                price=state_services.total_price + state_designs.total_price,
                font_weight="600",
            ),
            # on_mount=[
            #     state_quote_summary.total_price(
            #         state_designs.total_price, state_services.total_price
            #     ),
            # ],
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
