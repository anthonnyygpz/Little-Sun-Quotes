import reflex as rx


class InfoClientState(rx.State):
    name_client: str = ""
    phone_number: str = ""
    register_or_exist: bool = False

    def on_mount(self):
        self.name_client = ""
        self.phone_number = ""
        self.register_or_exist = False

    @rx.event
    def change_cheked(self, is_checked: bool):
        self.register_or_exist = is_checked
