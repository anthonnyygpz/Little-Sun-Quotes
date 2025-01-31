import reflex as rx

# from little_sun.states.nail_services import ServicesState
# from little_sun.utils.constants import Colors

from little_sun.repositories.services import ServicesState


def input_text(input_id, input_name, input_type, on_blur, text_value):
    """Create an input element with specific styling and attributes."""
    return rx.el.input(
        id=input_id,
        name=input_name,
        type=input_type,
        border_width="1px",
        border_color="#D1D5DB",
        _focus={
            "outline-style": "none",
            "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
            "--ring-color": "purple",
        },
        padding_left="0.75rem",
        padding_right="0.75rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.375rem",
        width="100%",
        placeholder=text_value,
        on_blur=on_blur,
    )


def create_checkbox(checkbox_id, checkbox_name, price, state):
    """Create a checkbox input element with specific styling."""
    return (
        rx.checkbox(
            checkbox_name,
            id=checkbox_id,
            name=checkbox_name,
            checked=state.is_checked[checkbox_name],
            on_click=lambda: [
                state.toggle_item(checkbox_name, price, checkbox_id),
            ],
            variant="surface",
            color_scheme="purple",
            default_checked=False,
        ),
    )
