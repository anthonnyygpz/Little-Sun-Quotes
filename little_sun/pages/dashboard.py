import reflex as rx

from little_sun.layouts.layouts import layout

# from ..views.header.navbar import navbar
from little_sun.sections.table_dashboard.table import main_table


def dashboard() -> rx.Component:
    return layout(
        rx.vstack(
            main_table(),
        )
    )
