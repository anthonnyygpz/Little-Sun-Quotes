import reflex as rx


def form(state_var, content):
    return rx.form(
        rx.box(
            content,
            gap="1rem",
            display="grid",
            grid_template_columns=rx.breakpoints(
                {
                    "0px": "repeat(1, minmax(0, 1fr))",
                    "768px": "repeat(2, minmax(0, 1fr))",
                }
            ),
            on_mount=lambda: [state_var.all_client_info],
        ),
    )
