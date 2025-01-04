import reflex as rx

from little_sun.utils.constants import Colors


def navbar():
    return rx.flex(
        rx.badge(
            rx.icon(tag="table-2", size=28, color=Colors.purple),
            rx.heading("Little Sun App", size="6", color=Colors.purple),
            border="0.2em solid",
            border_color=Colors.purple,
            bg=Colors.purple_degraded,
            radius="large",
            align="center",
            variant="surface",
            padding="0.65rem",
        ),
        # rx.spacer(),
        # rx.hstack(
        #     rx.logo(),
        #     rx.color_mode.button(),
        #     align="center",
        #     spacing="3",
        # ),
        spacing="2",
        flex_direction=["column", "column", "row"],
        align="center",
        width="100%",
        top="0px",
        padding_top="2em",
    )
