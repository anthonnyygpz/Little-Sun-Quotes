import reflex as rx

from little_sun.components.buttons import (
    clean_quote_button,
    generate_quote_button,
    update_quote_button,
)
from little_sun.repositories.create_quotes import CreateQuotes
from little_sun.repositories.designs import DesignsState
from little_sun.repositories.info_client import ClientsState
from little_sun.repositories.nail_size import NailSizesState
from little_sun.repositories.params_url import ParamsUrl
from little_sun.repositories.services import ServicesState
from little_sun.repositories.status import StatusState
from little_sun.repositories.update_quote import UpdateQuote
from little_sun.views.section_quote_generator.client_info import (
    client_information_section,
    client_update_section,
)
from little_sun.views.section_quote_generator.designs import designs_selection_section
from little_sun.views.section_quote_generator.nail_sizes import (
    nail_sizes_selection_section,
)
from little_sun.views.section_quote_generator.quote_summary import quote_summary_section
from little_sun.views.section_quote_generator.services import services_selection_section

from ..templates.base import base_template
from little_sun.components.labels import create_heading


def quote_generator() -> rx.Component:
    """Main page of the application."""
    return base_template(
        rx.box(
            rx.box(
                rx.match(
                    ParamsUrl.params_data["method"],
                    (
                        "POST",
                        rx.heading(
                            "Generar cotizaciones de uñas",
                            font_weight="700",
                            font_size="1.875rem",
                            line_height="2.25rem",
                            color_scheme="purple",
                            as_="h1",
                        ),
                    ),
                    (
                        "PUT",
                        rx.heading(
                            "Actualizar cotizacion.",
                            font_weight="700",
                            font_size="1.875rem",
                            line_height="2.25rem",
                            color_scheme="purple",
                            as_="h1",
                        ),
                    ),
                    rx.heading(
                        "Sin Seleccionar",
                        font_weight="700",
                        font_size="1.875rem",
                        line_height="2.25rem",
                        color_scheme="red",
                        as_="h1",
                    ),
                ),
                margin_bottom="2rem",
                text_align="center",
            ),
            rx.box(
                rx.icon_button(
                    "circle-arrow-left",
                    color_scheme="purple",
                    on_click=rx.redirect("http://localhost:3000/"),
                ),
            ),
            # Section info clients
            rx.match(
                ParamsUrl.params_data["method"],
                (
                    "POST",
                    client_information_section(
                        state_clients=ClientsState,
                    ),
                ),
                (
                    "PUT",
                    client_update_section(
                        state_clients=ClientsState,
                    ),
                ),
            ),
            # Section nail sizes
            nail_sizes_selection_section(
                state_nail_sizes=NailSizesState,
                label_text="Selecciona el tipo de escultura",
            ),
            # # Section services
            services_selection_section(
                state_services=ServicesState,
                label_text="Selecciona un servicio",
            ),
            # # Section designs
            designs_selection_section(
                state_designs=DesignsState,
                label_text="Selecciona un diseño",
            ),
            # # Section quote summary
            quote_summary_section(
                state_clients=ClientsState,
                state_nail_sizes=NailSizesState,
                state_services=ServicesState,
                state_designs=DesignsState,
            ),
            rx.match(
                ParamsUrl.params_data["method"],
                (
                    "PUT",
                    rx.box(
                        create_heading(text="Resumen de la cita"),
                        rx.radio(
                            ["Completed", "Pending", "Cancelled"],
                            default_value=StatusState.status,
                            on_change=StatusState.set_status,  # type: ignore
                            color_scheme="purple",
                            direction="row",
                            as_child=True,
                            required=True,
                        ),
                        background_color="#ffffff",
                        margin_bottom="2rem",
                        padding="1.5rem",
                        border_radius="0.5rem",
                        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
                    ),
                ),
            ),
            rx.flex(
                # button generate quote
                rx.match(
                    ParamsUrl.params_data["method"],
                    (
                        "PUT",
                        update_quote_button(
                            state_update_quote=UpdateQuote,
                            form_data={
                                "quote_id": ParamsUrl.params_data["quote_id"],
                                "client_id": ParamsUrl.params_data["id_client"],
                                "size_id": NailSizesState.size_id,
                                "service": ServicesState.service_selected,
                                "design": DesignsState.design_selected,
                                "name_client": ClientsState.name_client,
                                "phone_number": ClientsState.phone_number,
                                "total_price": ServicesState.total_price,
                                "status": StatusState.status,
                            },
                            url_redirect="http://localhost:3000/",
                        ),
                    ),
                    (
                        "POST",
                        generate_quote_button(
                            state_state=CreateQuotes,
                            form_data={
                                "size_id": NailSizesState.size_id,
                                "service": ServicesState.service_selected,
                                "design": DesignsState.design_selected,
                                "name_client": ClientsState.name_client,
                                "phone_number": ClientsState.phone_number,
                                "total_price_service": ServicesState.total_price,
                                "total_price_design": DesignsState.total_price,
                            },
                            url_redirect="http://localhost:3000/",
                        ),
                    ),
                ),
                # button clean all quotes
                clean_quote_button(),
                display="flex",
                justify_content="space-between",
            ),
            on_mount=lambda: [
                CreateQuotes.reset_all,
                ParamsUrl.get_method,
            ],
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
