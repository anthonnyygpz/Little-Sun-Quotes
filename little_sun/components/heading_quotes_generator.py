import reflex as rx
from little_sun.components.labels import heading
from little_sun.repositories.params_url import ParamsUrl


def heading_quote_generator():
    return (
        rx.box(
            rx.match(
                ParamsUrl.params_data["method"],
                (
                    "POST",
                    heading(
                        text="Generar cotizaciones de uñas",
                        font_weight="700",
                        font_size="1.875rem",
                        line_height="2.25rem",
                        color="purple",
                    ),
                ),
                (
                    "PUT",
                    heading(
                        text="Actualizar cotizacion.",
                        font_weight="700",
                        font_size="1.875rem",
                        line_height="2.25rem",
                        color="purple",
                    ),
                ),
                heading(
                    "Sin Seleccionar",
                    font_weight="700",
                    font_size="1.875rem",
                    line_height="2.25rem",
                    color="red",
                ),
            ),
            margin_bottom="2rem",
            text_align="center",
        ),
    )
