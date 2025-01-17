import reflex as rx

from little_sun.states.crud_dashboard import CRUDDashboard

from .components.row_tables import show_client, header_cell
from .components.buttons import add_client_button


def main_table():
    return rx.box(
        rx.fragment(
            rx.flex(
                rx.link(add_client_button(), href="/quote/POST/0/0"),
                rx.spacer(),
                # Aqui va lo que esta comendao hasta abajo
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
                        header_cell("Nombre", "user"),
                        header_cell("Tamaño de uña", "ruler"),
                        header_cell("Servicio", "hand"),
                        header_cell("Diseño", "eclipse"),
                        header_cell("Precio total", "dollar-sign"),
                        header_cell("Fecha de creacion", "calendar"),
                        header_cell("Estatus", "clock-10"),
                        header_cell("Acciones", "cog"),
                    ),
                ),
                rx.table.body(rx.foreach(CRUDDashboard.user, show_client)),
                variant="surface",
                size="3",
                width="100%",
                on_mount=lambda: [CRUDDashboard.view_quotes],
            ),
        ),
        width="100%",
    )

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
