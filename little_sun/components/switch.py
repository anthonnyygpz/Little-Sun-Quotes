import reflex as rx
from little_sun.repositories.info_client import ClientsState


def switch():
    return (
        rx.box(
            rx.text("Seleccionar registrar/existente"),
            rx.switch(
                checked=ClientsState.is_exists,
                on_change=[
                    ClientsState.change_existence_status,
                    ClientsState.reset_switch,
                ],
            ),
        ),
    )
