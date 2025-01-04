import reflex as rx
from ..templates.base import base_template
from ..views.client_info.client_information_secetion import (
    client_information_section,
)
from ..views.nail_sizes_selection.nail_sizes_selection_section import (
    nail_sizes_selection_section,
)
from ..views.service_selection.services_selection_section import (
    services_selection_section,
)
from ..views.designs_selection.designs_selection_section import (
    designs_selection_section,
)
from ..views.quote_summary.quote_summary_section import quote_summary_section
from ..components.buttons import (
    generate_quote_button,
    create_clean_quote_button,
)

from ..states.nail_sizes import NailSizesAPI
from ..states.nail_services import NailServicesAPI, NailServices
from ..states.designs import DesignsAPI
from ..states.nail_sizes import NailSizes
from ..utils.constants import Colors


def quote_generator() -> rx.Component:
    """Main page of the application."""
    return base_template(
        rx.box(
            rx.box(
                rx.heading(
                    "Generador de cotizaciones para uñas.",
                    font_weight="700",
                    font_size="1.875rem",
                    line_height="2.25rem",
                    color=Colors.purple,
                    as_="h1",
                ),
                margin_bottom="2rem",
                text_align="center",
            ),
            rx.box(
                rx.icon_button(
                    "circle-arrow-left",
                    bg=Colors.purple,
                    on_click=rx.redirect("http://localhost:3000/"),
                ),
            ),
            client_information_section(),
            nail_sizes_selection_section(
                items=NailSizesAPI,
                text="Selecciona el tipo de escultura",
            ),
            services_selection_section(
                items=NailServicesAPI,
                mount=NailServices,
                text="Selecciona un servicio",
            ),
            designs_selection_section(
                items=DesignsAPI, text="Selecciona un diseño"
            ),
            quote_summary_section(),
            rx.flex(
                generate_quote_button(),
                create_clean_quote_button(),
                display="flex",
                justify_content="space-between",
            ),
            on_mount=[NailSizes.on_mount],
            width="100%",
            style=rx.breakpoints(  # type: ignore
                {
                    "640px": {"max-width": "640px"},
                    "768px": {"max-width": "768px"},
                    "1024px": {"max-width": "1024px"},
                    "1280px": {"max-width": "1280px"},
                    "1536px": {"max-width": "1536px"},
                }
            ),
            margin_left="auto",
            margin_right="auto",
            padding_left="1rem",
            padding_right="1rem",
            padding_top="2rem",
            padding_bottom="2rem",
        )
    )
