import reflex as rx

from little_sun.components.forms import create_checkbox
from little_sun.components.pricing import create_price_span
from little_sun.components.section_banner import section_banner
from little_sun.repositories.services import ServicesState


def service():
    return section_banner(
        state_var=ServicesState,
        label_text="Selecciona un servicio",
        content=rx.box(
            rx.foreach(
                ServicesState.data,
                lambda item: rx.flex(
                    create_checkbox(
                        checkbox_id=f"{item.service_id}",
                        checkbox_name=f"{item.service_name}",
                        price=item.price,
                        state=ServicesState,
                    ),
                    create_price_span(price_text=f"${item.price}"),
                    display="flex",
                    align_items="center",
                ),
            ),
            on_mount=[ServicesState.all_services, ServicesState.reset_all],
            display="flex",
            flex_direction="column",
            gap="0.5rem",
        ),
    )
