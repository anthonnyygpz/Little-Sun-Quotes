import reflex as rx

from ...states.nail_sizes import NailSizes
from ...components.labels import create_heading
from ...utils.constants import Colors


def nail_sizes_selection_section(items, text):
    """Create the services selection section of the form."""
    return rx.box(
        create_heading(text),
        rx.box(
            rx.cond(
                items.loading,
                rx.spinner(),
                rx.cond(
                    items.error != "",
                    rx.text(items.error, color=Colors.error),
                    rx.foreach(
                        items.data,
                        lambda item: rx.button(
                            item.size_name,
                            on_click=lambda p=item: NailSizes.add_type_escultural(
                                p
                            ),
                            bg=rx.cond(
                                NailSizes.type_escultural == item.size_name,
                                Colors.purple,
                                Colors.white,
                            ),
                            color=rx.cond(
                                NailSizes.type_escultural == item.size_name,
                                Colors.white,
                                Colors.black,
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
