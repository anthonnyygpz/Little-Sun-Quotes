import reflex as rx
from ..views.header.navbar import navbar
from ..views.table_dashboard.table import main_table


def dashboard() -> rx.Component:
    return rx.vstack(
        navbar(),
        main_table(),
        width="100%",
        spacing="6",
        padding_x=["1.5em", "1.5em", "3em"],
    )
