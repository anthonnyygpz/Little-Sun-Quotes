from little_sun.components.labels import heading
import reflex as rx


def section_banner(state_var, label_text, content):
    return rx.box(
        heading(label_text),
        rx.cond(
            state_var.error,
            rx.text(state_var.error, color_scheme="red"),
            content,
        ),
        background_color="#ffffff",
        margin_bottom="2rem",
        padding="1.5rem",
        border_radius="0.5rem",
        box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
    )
