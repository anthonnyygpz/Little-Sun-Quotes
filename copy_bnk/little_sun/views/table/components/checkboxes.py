import reflex as rx


def heading(icon, label_text):
    return rx.hstack(
        rx.icon(icon, size=16, stroke_width=1.5),
        rx.text(label_text),
        align="center",
        spacing="2",
    )


def checkbox_services(state_services, label_text, icon, name):
    return rx.vstack(
        heading(icon, label_text),
        rx.vstack(
            rx.foreach(
                state_services.data,
                lambda item: rx.hstack(
                    rx.checkbox(
                        f"{item.service_name}",
                        on_change=lambda: state_services.handle_select(
                            item.service_name
                        ),
                        name=f"{name}{item.service_id}",
                    ),
                    width="100%",
                    spacing="2",
                ),
            ),
            bg="background",
            p="4",
            border_radius="md",
            border="1px solid",
            border_color="accent.5",
            width="100%",
            spacing="3",
        ),
    )


def checkbox_designs(state_designs, label_text, icon, name):
    return (
        rx.vstack(
            heading(icon, label_text),
            rx.vstack(
                rx.foreach(
                    state_designs.data,
                    lambda item: rx.hstack(
                        rx.checkbox(
                            f"{item.design_name}",
                            on_change=lambda: state_designs.handle_select(
                                item.design_name
                            ),
                            name=f"{name}{item.design_id}",
                        ),
                        width="100%",
                        spacing="2",
                    ),
                ),
                bg="background",
                p="4",
                border_radius="md",
                border="1px solid",
                border_color="accent.5",
                width="100%",
                spacing="3",
            ),
        ),
    )


def select(state):
    return rx.vstack(
        rx.box(
            rx.text(
                "Servicios seleccionados:",
                font_weight="bold",
                mb="2",
            ),
            rx.box(
                rx.foreach(
                    state.selected,
                    lambda item: rx.hstack(
                        rx.text(item),
                        bg="accent.2",
                        p="2",
                        border_radius="md",
                        mr="2",
                        mb="2",
                    ),
                ),
            ),
            bg="background",
            p="4",
            border_radius="md",
            width="100%",
            display=rx.cond(state.selected, "block", "none"),
        ),
    )
