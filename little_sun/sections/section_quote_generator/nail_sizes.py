import reflex as rx
from little_sun.components.labels import heading


def nail_sizes_selection_section(state_var, label_text):
    """Create the services selection section of the form."""
    return
    rx.box(
        heading(label_text),
        rx.cond(
            state_var.error,
            rx.text(state_var.error, color_scheme="red"),
            rx.box(
                rx.foreach(
                    state_var.data,
                    lambda item: rx.skeleton(
                        rx.button(
                            item.size_name,
                            on_click=lambda: [
                                state_var.update_type_escultural(item.size_name),
                                state_var.update_size_id(item.size_id),
                            ],
                            bg=rx.cond(
                                state_var.type_escultural == item.size_name,
                                "purple",
                                "white",
                            ),
                            color=rx.cond(
                                state_var.type_escultural == item.size_name,
                                "white",
                                "black",
                            ),
                            margin="0.5em",
                            padding="1em",
                            border_radius="md",
                            display="flex",
                            align_items="center",
                        ),
                        height="10px",
                        loading=False,
                    ),
                ),
                on_mount=lambda: [
                    state_var.all_nail_sizes,
                    state_var.reset_all,
                ],
                display="flex",
                flex_direction="column",
                gap="0.5rem",
            ),
        ),
        background_color="#ffffff",
        margin_bottom="2rem",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )
