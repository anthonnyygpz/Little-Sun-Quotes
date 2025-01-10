import reflex as rx

from ..components.buttons import (
    clean_quote_button,
    generate_quote_button,
)
from ..states.clients import ClientsState
from ..states.designs import DesignsState
from ..states.nail_services import ServicesState
from ..states.nail_sizes import NailSizesState
from ..states.state import State
from ..templates.base import base_template
from ..utils.constants import Colors
from ..views.client_info.client_information_secetion import (
    client_information_section,
)
from ..views.designs_selection.designs_selection_section import (
    designs_selection_section,
)
from ..views.nail_sizes_selection.nail_sizes_selection_section import (
    nail_sizes_selection_section,
)
from ..views.quote_summary.quote_summary_section import quote_summary_section
from ..views.service_selection.services_selection_section import (
    services_selection_section,
)


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
            # Section info clients
            client_information_section(
                state_clients=ClientsState,
            ),
            # Section nail sizes
            nail_sizes_selection_section(
                state_nail_sizes=NailSizesState,
                label_text="Selecciona el tipo de escultura",
            ),
            # Section services
            services_selection_section(
                state_services=ServicesState,
                label_text="Selecciona un servicio",
            ),
            # Section designs
            designs_selection_section(
                state_designs=DesignsState,
                label_text="Selecciona un diseño",
            ),
            # Section quote summary
            quote_summary_section(
                state_clients=ClientsState,
                state_nail_sizes=NailSizesState,
                state_services=ServicesState,
                state_state=State,
            ),
            rx.flex(
                # button generate quote
                generate_quote_button(
                    state_state=State,
                    form_data={
                        "size": NailSizesState.id_type_escultural,
                        "service": ServicesState.items,
                        "name_client": ClientsState.name_client,
                        "phone_number": ClientsState.phone_number,
                        "total_price": ServicesState.total_price,
                    },
                    url_redirect="http://localhost:3000/",
                ),
                # button clean all quotes
                clean_quote_button(state_services=ServicesState),
                display="flex",
                justify_content="space-between",
            ),
            on_mount=[NailSizesState.on_mount],
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
