import reflex as rx

from little_sun.repositories.all_appoiments import AllAppoiments
from little_sun.repositories.delete_quote import DeleteQuote
from .components.status_badge import status_badge


def show_quote(user):
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
                ("Completed", status_badge("Completed")),
                ("Pending", status_badge("Pending")),
                ("Cancelled", status_badge("Cancelled")),
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
                        DeleteQuote.delete_quote(user.quote_id),
                        rx.toast(DeleteQuote.success),
                        AllAppoiments.all_appoiments,
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
