import reflex as rx


def switch_selection(state_clients):
    return (
        rx.box(
            rx.text("Seleccionar registrar/existente"),
            rx.switch(
                checked=state_clients.register_or_exist,
                on_change=[
                    state_clients.change_cheked,
                    state_clients.switch,
                ],
            ),
        ),
    )
