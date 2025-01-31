import reflex as rx

from little_sun.components.labels import heading
from little_sun.components.pricing import create_price_row
from little_sun.components.section_banner import section_banner
from little_sun.repositories.designs import DesignsState
from little_sun.repositories.info_client import ClientsState
from little_sun.repositories.nail_size import NailSizesState
from little_sun.repositories.services import ServicesState
from little_sun.repositories.quote_summary import QuoteSummary


def quote_summary():
    return section_banner(
        state_var=QuoteSummary,
        label_text="Resumen de la cita",
        content=rx.box(
            heading(text=f"Nombre del cliente: {ClientsState.name_client}"),
            heading(text=f"Tipo de escultura usado: {NailSizesState.type_escultural}"),
            rx.foreach(
                ServicesState.service_selected,
                lambda item: create_price_row(
                    label_text=item.name, price=item.price, color="green"
                ),
            ),
            rx.foreach(
                DesignsState.design_selected,
                lambda item: create_price_row(
                    label_text=item.name, price=item.price, color="green"
                ),
            ),
            rx.divider(),
            create_price_row(
                label_text="Total:",
                price=ServicesState.total_price + DesignsState.total_price,
                font_weight="600",
            ),
            display="flex",
            flex_direction="column",
            gap="0.5rem",
        ),
    )
