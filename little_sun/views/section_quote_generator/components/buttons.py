import reflex as rx


def switch_selection(state_clients):
    return (
        rx.box(
            rx.text("Seleccionar registrar/existente"),
            rx.switch(
                checked=state_clients.is_exists,
                on_change=[
                    state_clients.change_existence_status,
                    state_clients.reset_switch,
                ],
            ),
        ),
    )
