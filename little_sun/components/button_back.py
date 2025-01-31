import reflex as rx


def button_back():
    return (
        rx.box(
            rx.icon_button(
                "circle-arrow-left",
                color_scheme="purple",
                on_click=rx.redirect("http://localhost:3000/"),
            ),
        ),
    )
