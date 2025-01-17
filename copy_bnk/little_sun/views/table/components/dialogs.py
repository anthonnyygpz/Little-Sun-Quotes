import reflex as rx
from little_sun.states.nail_services import ServicesState
from little_sun.states.designs import DesignsState
from little_sun.states.crud_dashboard import CRUDDashboard
from little_sun.states.nail_sizes import NailSizesState
from ....components.form_field import form_field
from .checkboxes import select, checkbox_designs, checkbox_services


def update_customer_dialog(user):
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("square-pen", size=22),
                rx.text("Editar", size="3"),
                color_scheme="blue",
                size="2",
                variant="solid",
            ),
        ),
        rx.dialog.content(
            rx.hstack(
                rx.badge(
                    rx.icon(tag="square-pen", size=34),
                    color_scheme="grass",
                    radius="full",
                    padding="0.65rem",
                ),
                rx.vstack(
                    rx.dialog.title(
                        "Editar Cliente",
                        weight="bold",
                        margin="0",
                    ),
                    rx.dialog.description(
                        "Editar el informacion del cliente",
                    ),
                    spacing="1",
                    height="100%",
                    align_items="start",
                ),
                height="100%",
                spacing="4",
                margin_bottom="1.5em",
                align_items="center",
                width="100%",
            ),
            rx.flex(
                rx.form.root(
                    rx.flex(
                        # quote_id
                        rx.box(
                            rx.text_field(value=f"{user.quote_id}", name="quote_id"),
                            display="None",
                        ),
                        # client_id
                        rx.box(
                            rx.text_field(value=f"{user.client_id}", name="client_id"),
                            display="None",
                        ),
                        # Name
                        form_field(
                            "Nombre",
                            "Nombre del cliente",
                            "text",
                            "name",
                            "user",
                            f"{user.name}",
                        ),
                        # Size name
                        rx.select.root(
                            rx.select.trigger(placeholder="No Seleccionado"),
                            rx.select.content(
                                rx.select.group(
                                    rx.foreach(
                                        NailSizesState.data,
                                        lambda item: rx.select.item(
                                            f"{item.size_name}",
                                            value=f"{item.size_name}",
                                            name="size_name",
                                        ),
                                    ),
                                ),
                            ),
                            value=NailSizesState.name_size,
                            on_change=NailSizesState.set_name_size,  # type: ignore
                        ),
                        rx.box(
                            rx.text(
                                "Tamaño seleccionado:",
                                font_weight="bold",
                                mb="2",
                            ),
                            rx.box(
                                rx.text(NailSizesState.name_size),
                                bg="accent.2",
                                p="2",
                                border_radius="md",
                                mr="2",
                                mb="2",
                            ),
                            bg="background",
                            p="4",
                            border_radius="md",
                            width="100%",
                            display=rx.cond(NailSizesState.name_size, "block", "none"),
                        ),
                        # Services
                        checkbox_services(
                            state_services=ServicesState,
                            label_text="Servicios",
                            icon="hand",
                            name="service_",
                        ),
                        select(state=ServicesState),
                        # Designs
                        checkbox_designs(
                            state_designs=DesignsState,
                            label_text="Diseño",
                            icon="eclipse",
                            name="design_",
                        ),
                        select(state=DesignsState),
                        # Total_amount
                        form_field(
                            "Precio Total ($)",
                            "Precio",
                            "num",
                            "total_amount",
                            "dollar-sign",
                            f"{user.total_amount}",
                        ),
                        # Created_at
                        form_field(
                            "Fecha de creacion",
                            "Fecha de creacion",
                            "text",
                            "created_at",
                            "calendar",
                            f"{user.created_at}",
                            True,
                        ),
                        # Status
                        rx.vstack(
                            rx.hstack(
                                rx.icon("clock", size=16, stroke_width=1.5),
                                rx.text("Status"),
                                align="center",
                                spacing="2",
                            ),
                            rx.radio(
                                ["Completed", "Pending", "Cancelled"],
                                default_value=user.status,
                                name="status",
                                direction="row",
                                as_child=True,
                                required=True,
                            ),
                        ),
                        on_mount=lambda: [
                            ServicesState.fetch_data,
                            DesignsState.fetch_data,
                            NailSizesState.fetch_data,
                        ],
                        direction="column",
                        spacing="3",
                    ),
                    rx.flex(
                        rx.dialog.close(
                            rx.button(
                                "Cancelar",
                                variant="soft",
                                color_scheme="gray",
                            ),
                        ),
                        rx.form.submit(
                            rx.dialog.close(
                                rx.button("Actualizar cliente", type="submit"),
                            ),
                            as_child=True,
                        ),
                        padding_top="2em",
                        spacing="3",
                        mt="4",
                        justify="end",
                    ),
                    on_mount=lambda: [
                        DesignsState.on_mount,
                        ServicesState.on_mount,
                        NailSizesState.on_mount,
                    ],
                    on_submit=lambda: [CRUDDashboard.update_quotes],
                    reset_on_submit=False,
                ),
                width="100%",
                direction="column",
                spacing="4",
            ),
            max_width="450px",
            padding="1.5em",
            border=f"2px solid {rx.color('accent', 7)}",
            border_radius="25px",
        ),
    )
