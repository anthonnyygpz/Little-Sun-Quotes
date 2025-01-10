import reflex as rx

from ...components.labels import create_heading
from ...utils.constants import Colors


def nail_sizes_selection_section(state_nail_sizes, label_text):
    """Create the services selection section of the form."""
    return rx.box(
        create_heading(label_text),
        rx.box(
            rx.cond(
                state_nail_sizes.loading,
                rx.spinner(),
                rx.cond(
                    state_nail_sizes.error != "",
                    rx.text(state_nail_sizes.error, color=Colors.error),
                    rx.foreach(
                        state_nail_sizes.data,
                        lambda item: rx.button(
                            item.size_name,
                            on_click=lambda p=item: state_nail_sizes.add_type_escultural(
                                p
                            ),
                            bg=rx.cond(
                                state_nail_sizes.type_escultural == item.size_name,
                                Colors.purple,
                                Colors.white,
                            ),
                            color=rx.cond(
                                state_nail_sizes.type_escultural == item.size_name,
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
            on_mount=[state_nail_sizes.fetch_data, state_nail_sizes.on_mount],
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
