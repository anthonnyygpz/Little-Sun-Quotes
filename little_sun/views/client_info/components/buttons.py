import reflex as rx
from ....states.info_client import InfoClientState


def switch_selection():
    return (
        rx.box(
            rx.text("Seleccionar registrar/existente"),
            rx.switch(
                checked=InfoClientState.register_or_exist,
                on_change=[
                    InfoClientState.change_cheked,
                    InfoClientState.switch,
                ],
            ),
        ),
    )
