import reflex as rx

from little_sun.repositories.all_appoiments import AllAppoiments
from .components.header_cell import headerCell
from .components.add_client_button import add_client_button
from .show_quotes import show_quote


def main_table():
    return rx.box(
        rx.fragment(
            rx.flex(
                rx.link(add_client_button(), href="/quote/POST/0/0"),
                rx.spacer(),
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
                        headerCell("Nombre", "user"),
                        headerCell("Tamaño de uña", "ruler"),
                        headerCell("Servicio", "hand"),
                        headerCell("Diseño", "eclipse"),
                        headerCell("Precio total", "dollar-sign"),
                        headerCell("Fecha de creacion", "calendar"),
                        headerCell("Estatus", "clock-10"),
                        headerCell("Acciones", "cog"),
                    ),
                ),
                rx.table.body(rx.foreach(AllAppoiments.data, show_quote)),
                variant="surface",
                size="3",
                width="100%",
                on_mount=lambda: [
                    AllAppoiments.all_appoiments,
                ],
            ),
        ),
        width="100%",
    )
