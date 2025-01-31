import reflex as rx
from little_sun.components.section_banner import section_banner
from little_sun.repositories.params_url import ParamsUrl
from little_sun.components.labels import heading
from little_sun.repositories.status import StatusState


def status():
    return (
        rx.match(
            ParamsUrl.params_data["method"],
            (
                "PUT",
                section_banner(
                    state_var=StatusState,
                    label_text="",
                    content=rx.radio(
                        ["Completed", "Pending", "Cancelled"],
                        default_value=StatusState.status,
                        on_change=StatusState.set_status,  # type: ignore
                        color_scheme="purple",
                        direction="row",
                        as_child=True,
                        required=True,
                    ),
                ),
            ),
        ),
    )
