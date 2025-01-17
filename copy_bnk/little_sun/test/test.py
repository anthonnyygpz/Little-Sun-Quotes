import reflex as rx


class State(rx.State):
    # Variable para almacenar los datos
    item_data: dict[str, int] = {}

    def handle_auth(self):
        auth_params = self.router.page.params
        print(f"Query params: {auth_params}")
        self.item_data = auth_params
        # if auth_params.get("code") and auth_params.get("state"):
        #     self.auth_code = auth_params["code"]
        #     self.auth_state = auth_params["state"]


def item_details():
    """Página de detalles del item."""
    return rx.box(
        rx.heading(f"Detalles del Item {State.item_data.values()}"),
        # rx.text(f"Nombre: {State.item_data['name']}"),
        # rx.text(f"Precio: ${State.item_data['price']}"),
        on_mount=lambda: State.handle_auth,
    )


def test():
    """Página principal con enlaces a items."""
    return rx.box(
        rx.heading("Lista de Items"),
        rx.link("Ver Item 1", href="/item/1"),
        rx.link("Ver Item 2", href="/item/2"),
        rx.link("Ver Item 3", href="/item/3"),
    )


# Configuración de la aplicación
app = rx.App()

# Agregar rutas
