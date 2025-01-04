import reflex as rx

from little_sun.states.crud_dashboard import CRUDDashboard

from ..backend.backend import State
from ..components.form_field import form_field

from ..components.status_badges import status_badge


def show_client(user):
    """Show a client in a table row."""

    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.size_name),
        rx.table.cell(user.services),
        rx.table.cell(user.designs),
        rx.table.cell(user.total_amount),
        rx.table.cell(user.created_at),
        rx.table.cell(
            rx.match(
                user.status,
                ("Delivered", status_badge("Delivered")),
                ("Pending", status_badge("Pending")),
                ("Cancelled", status_badge("Cancelled")),
                status_badge("Pending"),
            )
        ),
        rx.table.cell(
            rx.hstack(
                # Fuera de servicio
                # update_customer_dialog(user),
                rx.icon_button(
                    rx.icon("trash-2", size=22),
                    on_click=lambda: CRUDDashboard.delete_quotes(user.quote_id),
                    size="2",
                    variant="solid",
                    color_scheme="red",
                ),
            )
        ),
        on_mount=CRUDDashboard.view_quotes,
        style={"_hover": {"bg": rx.color("gray", 3)}},  # type: ignore
        align="center",
    )


def add_client_button() -> rx.Component:
    return rx.button(
        rx.icon("plus", size=26),
        rx.text("Agregar cliente", size="4", display=["none", "none", "block"]),
        on_click=rx.redirect("http://localhost:3000/quote/"),
        bg="#7C3AED",
        size="3",
    )


def update_customer_dialog(user):
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("square-pen", size=22),
                rx.text("Editar", size="3"),
                color_scheme="blue",
                size="2",
                variant="solid",
                # on_click=lambda: State.get_user(user),
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
                        form_field(
                            "Email",
                            "user@reflex.dev",
                            "text",
                            "size_name",
                            "ruler",
                            f"{user.size_name}",
                        ),
                        # Services
                        form_field(
                            "Servicio",
                            "Servicio",
                            "text",
                            "services",
                            "hand",
                            f"{user.services}",
                        ),
                        # Designs
                        form_field(
                            "Diseño",
                            "Customer Address",
                            "text",
                            "designs",
                            "eclipse",
                            f"{user.designs}",
                        ),
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
                        ),
                        # Payments
                        # form_field(
                        #     "Payment ",
                        #     "Customer Payment",
                        #     "number",
                        #     "payments",
                        #     "dollar-sign",
                        #     user.payments.to(str),
                        # ),
                        # Status
                        rx.vstack(
                            rx.hstack(
                                rx.icon("clock", size=16, stroke_width=1.5),
                                rx.text("Status"),
                                align="center",
                                spacing="2",
                            ),
                            rx.radio(
                                ["Delivered", "Pending", "Cancelled"],
                                default_value=user.status,
                                name="status",
                                direction="row",
                                as_child=True,
                                required=True,
                            ),
                        ),
                        direction="column",
                        spacing="3",
                    ),
                    rx.flex(
                        rx.dialog.close(
                            rx.button(
                                "Cancel",
                                variant="soft",
                                color_scheme="gray",
                            ),
                        ),
                        rx.form.submit(
                            rx.dialog.close(
                                rx.button("Update Customer"),
                            ),
                            as_child=True,
                        ),
                        padding_top="2em",
                        spacing="3",
                        mt="4",
                        justify="end",
                    ),
                    on_submit=CRUDDashboard.update_quotes,
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


def _header_cell(text: str, icon: str):
    return rx.table.column_header_cell(
        rx.hstack(
            rx.icon(icon, size=18),
            rx.text(text),
            align="center",
            spacing="2",
        ),
    )


def main_table():
    return rx.fragment(
        rx.flex(
            add_client_button(),
            rx.spacer(),
            # rx.cond(
            #     State.sort_reverse,
            #     rx.icon(
            #         "arrow-down-z-a",
            #         size=28,
            #         stroke_width=1.5,
            #         cursor="pointer",
            #         on_click=State.toggle_sort,
            #     ),
            #     rx.icon(
            #         "arrow-down-a-z",
            #         size=28,
            #         stroke_width=1.5,
            #         cursor="pointer",
            #         on_click=State.toggle_sort,
            #     ),
            # ),
            # rx.select(
            #     [
            #         "name",
            #         "email",
            #         "phone",
            #         "address",
            #         "payments",
            #         "date",
            #         "status",
            #     ],
            #     placeholder="Sort By: Name",
            #     size="3",
            #     on_change=lambda sort_value: State.sort_values(sort_value),
            # ),
            # rx.input(
            #     rx.input.slot(rx.icon("search")),
            #     placeholder="Search here...",
            #     size="3",
            #     max_width="225px",
            #     width="100%",
            #     variant="surface",
            #     on_change=lambda value: State.filter_values(value),
            # ),
            justify="end",
            align="center",
            spacing="3",
            wrap="wrap",
            width="100%",
            padding_bottom="1em",
        ),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    _header_cell("Nombre", "user"),
                    _header_cell("Tamaño de uña", "ruler"),
                    _header_cell("Servicio", "hand"),
                    _header_cell("Diseño", "eclipse"),
                    _header_cell("Precio total", "dollar-sign"),
                    _header_cell("Fecha de creacion", "calendar"),
                    _header_cell("Estatus", "clock-10"),
                    _header_cell("Acciones", "cog"),
                ),
            ),
            # rx.table.body(rx.foreach(State.users, show_customer)),
            rx.table.body(rx.foreach(CRUDDashboard.user, show_client)),
            variant="surface",
            size="3",
            width="100%",
            on_mount=State.load_entries,
        ),
    )
