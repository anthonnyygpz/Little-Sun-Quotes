import reflex as rx

from little_sun.utils.constants import Colors


def create_button(text, on_clicked):
    return rx.el.button(
        text,
        background_color=Colors.purple,
        _focus={
            "outline-style": "none",
            "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
            "--ring-opacity": "0.5",
            "--ring-color": Colors.purple,
        },
        _hover={"background-color": Colors.purple},
        padding_left="1.5rem",
        padding_right="1.5rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.375rem",
        color="#ffffff",
        on_click=on_clicked,
    )


def generate_quote_button(state_state, form_data, url_redirect: str = ""):
    """Create a button for generating a quote."""
    return rx.el.button(
        " Generar cita ",
        background_color=Colors.purple,
        _focus={
            "outline-style": "none",
            "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
            "--ring-opacity": "0.5",
            "--ring-color": Colors.purple,
        },
        _hover={"background-color": Colors.purple},
        padding_left="1.5rem",
        padding_right="1.5rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.375rem",
        color="#ffffff",
        on_click=lambda: [
            state_state.upload_data(form_data),
            rx.redirect(url_redirect),
        ],
    )


def update_quote_button(state_crud_dashboard, form_data, url_redirect: str = ""):
    return rx.el.button(
        "Actulizar cita",
        background_color=Colors.purple,
        _focus={
            "outline-style": "none",
            "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
            "--ring-opacity": "0.5",
            "--ring-color": Colors.purple,
        },
        _hover={"background-color": Colors.purple},
        padding_left="1.5rem",
        padding_right="1.5rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.375rem",
        color="#ffffff",
        on_click=lambda: [
            state_crud_dashboard.update_form_data(form_data),
            # rx.redirect(url_redirect),
        ],
    )


def create_save_quote_button():
    """Create a button for saving a quote."""
    return rx.el.button(
        " Save Quote ",
        background_color="#E5E7EB",
        _focus={
            "outline-style": "none",
            "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
            "--ring-color": "#9CA3AF",
            "--ring-opacity": "0.5",
        },
        _hover={"background-color": "#D1D5DB"},
        padding_left="1.5rem",
        padding_right="1.5rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.375rem",
        color="#1F2937",
    )


def clean_quote_button(state_services):
    """Create a button for saving a quote."""
    return rx.el.button(
        " Borrar presupuesto ",
        background_color="#E5E7EB",
        _focus={
            "outline-style": "none",
            "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
            "--ring-color": "red",
            "--ring-opacity": "0.5",
        },
        _hover={"background-color": "red"},
        padding_left="1.5rem",
        padding_right="1.5rem",
        padding_top="0.5rem",
        padding_bottom="0.5rem",
        border_radius="0.375rem",
        color="#1F2937",
        on_click=[state_services.delete, state_services.delete],
    )


def create_view_saved_quotes_button():
    """Create a floating button for viewing saved quotes."""
    return rx.el.button(
        rx.icon(
            alt="View Saved Quotes",
            tag="list",
            height="1.5rem",
            width="1.5rem",
        ),
        background_color=Colors.purple,
        _focus={
            "outline-style": "none",
            "box-shadow": "var(--tw-ring-inset) 0 0 0 calc(2px + var(--tw-ring-offset-width)) var(--tw-ring-color)",
            "--ring-opacity": "0.5",
            "--ring-color": Colors.purple,
        },
        _hover={"background-color": Colors.purple},
        padding="1rem",
        border_radius="9999px",
        box_shadow="0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
        color="#ffffff",
    )
