import reflex as rx

from little_sun.states.crud_dashboard import CRUDDashboard

from ....components.status_badges import status_badge


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
                ("Completed", status_badge("Completo")),
                ("Pending", status_badge("Pendiente")),
                ("Cancelled", status_badge("Cancelado")),
                status_badge("Pending"),
            )
        ),
        rx.table.cell(
            rx.hstack(
                rx.link(
                    rx.button(
                        rx.icon("square-pen", size=22),
                        rx.text("Editar", size="3"),
                        color_scheme="blue",
                        size="2",
                        variant="solid",
                    ),
                    href=f"/quote/PUT/{user.quote_id}/{user.client_id}",
                ),
                rx.icon_button(
                    rx.icon("trash-2", size=22),
                    on_click=lambda: [
                        CRUDDashboard.delete_quotes(user.quote_id),
                        rx.toast(CRUDDashboard.successfully_delete),
                        CRUDDashboard.view_quotes,
                    ],
                    size="2",
                    variant="solid",
                    color_scheme="red",
                ),
            )
        ),
        style={"_hover": {"bg": rx.color("gray", 3)}},  # type: ignore
        align="center",
    )


def header_cell(text: str, icon: str):
    return rx.table.column_header_cell(
        rx.hstack(
            rx.icon(icon, size=18),
            rx.text(text),
            align="center",
            spacing="2",
        ),
    )
