from little_sun.components.section_banner import section_banner
from little_sun.repositories.nail_size import NailSizesState
from little_sun.components.labels import heading
import reflex as rx


def sculping_nail_size():
    return section_banner(
        state_var=NailSizesState,
        label_text="Selecciona el tipo de escultura",
        content=rx.box(
            rx.foreach(
                NailSizesState.data,
                lambda item: rx.skeleton(
                    rx.button(
                        item.size_name,
                        on_click=lambda: [
                            NailSizesState.update_type_escultural(item.size_name),
                            NailSizesState.update_size_id(item.size_id),
                        ],
                        bg=rx.cond(
                            NailSizesState.type_escultural == item.size_name,
                            "purple",
                            "white",
                        ),
                        color=rx.cond(
                            NailSizesState.type_escultural == item.size_name,
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
                NailSizesState.all_nail_sizes,
                NailSizesState.reset_all,
            ],
            display="flex",
            flex_direction="column",
            gap="0.5rem",
        ),
    )
