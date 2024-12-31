import reflex as rx

from little_sun.states.clients import ClientsAPI
from little_sun.states.designs import DesignsAPI
from little_sun.states.info_client import InfoClientState
from little_sun.states.nail_services import NailServices, NailServicesAPI
from little_sun.states.nail_sizes import NailSizes, NailSizesAPI


from little_sun.componets.buttons import *
from ..componets.forms import *
from ..componets.labels import *
from ..componets.pricing import *


def create_client_information_section():
    """Create the client information section of the form."""
    return rx.box(
        create_heading(text="Informacion del cliente"),
        rx.cond(
            InfoClientState.register_or_exist,
            rx.form(
                rx.box(
                    rx.box(
                        create_label(label_text="Nombre del cliente"),
                        rx.select.root(
                            rx.select.trigger(placeholder="No Seleccionado"),
                            rx.select.content(
                                rx.select.group(
                                    rx.foreach(
                                        ClientsAPI.data,
                                        lambda item: rx.select.item(
                                            f"{item.name}",
                                            value=f"{item.name}",
                                        ),
                                    ),
                                ),
                            ),
                            value=f"{InfoClientState.name_client}",
                            on_change=InfoClientState.set_name_client,  # type: ignore
                        ),
                    ),
                    rx.text(InfoClientState.name_client),
                    gap="1rem",
                    display="grid",
                    grid_template_columns=rx.breakpoints(
                        {
                            "0px": "repeat(1, minmax(0, 1fr))",
                            "768px": "repeat(2, minmax(0, 1fr))",
                        }
                    ),
                    on_mount=lambda: ClientsAPI.fetch_data,
                ),
            ),
            rx.form(
                rx.box(
                    rx.box(
                        create_label(label_text="Nombre del cliente"),
                        create_input(
                            input_id="clientName",
                            input_name="clientName",
                            input_type="text",
                            on_blur=InfoClientState.set_name_client,  # type: ignore
                            text_value=InfoClientState.name_client,
                        ),
                    ),
                    rx.box(
                        create_label(
                            label_text="Numero de telefono (Opcional)"
                        ),
                        create_input(
                            input_id="clientNumber",
                            input_name="clientNumber",
                            input_type="text",
                            on_blur=InfoClientState.set_phone_number,  # type: ignore
                            text_value=InfoClientState.phone_number,
                        ),
                    ),
                    on_mount=[InfoClientState.on_mount],
                    gap="1rem",
                    display="grid",
                    grid_template_columns=rx.breakpoints(
                        {
                            "0px": "repeat(1, minmax(0, 1fr))",
                            "768px": "repeat(2, minmax(0, 1fr))",
                        }
                    ),
                )
            ),
        ),
        rx.box(
            rx.text("Seleccionar registrar/existente"),
            rx.switch(
                checked=InfoClientState.register_or_exist,
                on_change=InfoClientState.change_cheked,
            ),
        ),
        bacspaceround_color="#ffffff",
        margin_bottom="2rem",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )


def create_nail_sizes_selection_section(items, text):
    """Create the services selection section of the form."""
    return rx.box(
        create_heading(text),
        rx.box(
            rx.cond(
                items.loading,
                rx.spinner(),
                rx.cond(
                    items.error != "",
                    rx.text(items.error, color="red"),
                    rx.foreach(
                        items.data,
                        lambda item: rx.button(
                            item.size_name,
                            on_click=lambda p=item: NailSizes.add_type_escultural(
                                p
                            ),
                            bg=rx.cond(
                                NailSizes.type_escultural == item.size_name,
                                "#7C3AED",
                                "#f1f1f1",
                            ),
                            color=rx.cond(
                                NailSizes.type_escultural == item.size_name,
                                "white",
                                "black",
                            ),
                            margin="0.5em",
                            padding="1em",
                            border_radius="md",
                            display="flex",
                            align_items="center",
                        ),
                    ),
                ),
            ),
            on_mount=[items.fetch_data, NailSizes.on_mount],
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


def create_services_selection_section(items, mount, text):
    """Create the services selection section of the form."""
    return rx.box(
        create_heading(text),
        rx.box(
            rx.cond(
                items.loading == False,
                rx.spinner(),
                rx.cond(
                    items.error != "",
                    rx.text(items.error, color="red"),
                    rx.foreach(
                        items.data,
                        lambda item: rx.flex(
                            create_checkbox(
                                checkbox_id=f"{item.service_id}",
                                checkbox_name=f"{item.service_name}",
                                price=item.price,
                                category="service",
                            ),
                            create_price_span(price_text=f"${item.price}"),
                            display="flex",
                            align_items="center",
                        ),
                    ),
                ),
            ),
            on_mount=[items.fetch_data, mount.on_mount],
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


def create_designs_selection_section(items, text):
    """Create the services selection section of the form."""
    return rx.box(
        create_heading(text),
        rx.box(
            rx.cond(
                items.loading == True,
                rx.spinner(),
                rx.cond(
                    items.error != "",
                    rx.text(items.error, color="red"),
                    rx.foreach(
                        items.data,
                        lambda item: rx.flex(
                            create_checkbox(
                                checkbox_id=f"{item.design_id}",
                                checkbox_name=f"{item.design_name}",
                                price=item.price,
                                category="service",
                            ),
                            create_price_span(price_text=f"${item.price}"),
                            display="flex",
                            align_items="center",
                        ),
                    ),
                ),
            ),
            on_mount=[items.fetch_data],
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


def create_quote_summary_section():
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
            on_mount=[NailSizes.on_mount, NailServices.on_mount],  # type: ignore
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


def quote_generator_view():
    """Main view for the quote generator."""
    return rx.box(
        rx.box(
            rx.heading(
                "Generador de cotizaciones para uñas.",
                font_weight="700",
                font_size="1.875rem",
                line_height="2.25rem",
                color="#7C3AED",
                as_="h1",
            ),
            margin_bottom="2rem",
            text_align="center",
        ),
        create_client_information_section(),
        create_nail_sizes_selection_section(
            items=NailSizesAPI,
            text="Selecciona el tipo de escultura",
        ),
        create_services_selection_section(
            items=NailServicesAPI,
            mount=NailServices,
            text="Selecciona un servicio",
        ),
        create_designs_selection_section(
            items=DesignsAPI, text="Selecciona un diseño"
        ),
        create_quote_summary_section(),
        rx.flex(
            create_generate_quote_button(),
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
