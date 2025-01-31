import reflex as rx

from little_sun.components.button_back import button_back
from little_sun.components.heading_quotes_generator import heading_quote_generator
from little_sun.repositories.create_quotes import CreateQuotes
from little_sun.repositories.params_url import ParamsUrl
from little_sun.sections import (
    buttons,
    design,
    quote_summary,
    service,
    sculping_nail_size,
    info_client,
    status,
)

from little_sun.layouts.layouts import layout


def quote_generator() -> rx.Component:
    return layout(
        rx.box(
            heading_quote_generator(),
            button_back(),
            info_client.info_client(),
            sculping_nail_size.sculping_nail_size(),
            service.service(),
            design.design(),
            status.status(),
            quote_summary.quote_summary(),
            buttons.buttons(),
            on_mount=lambda: [
                CreateQuotes.reset_all,
                ParamsUrl.get_method,
            ],
            width="100%",
            style=rx.breakpoints(  # type: ignore
                {
                    "640px": {"max-width": "640px"},
                    "768px": {"max-width": "768px"},
                    "1024px": {"max-width": "1024px"},
                    "1280px": {"max-width": "1280px"},
                    "1536px": {"max-width": "1536px"},
                }
            ),
            margin_left="auto",
            margin_right="auto",
            padding_left="1rem",
            padding_right="1rem",
            padding_top="2rem",
            padding_bottom="2rem",
        )
    )
