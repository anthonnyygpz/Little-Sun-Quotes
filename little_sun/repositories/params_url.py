from typing import Dict
import reflex as rx


class ParamsUrl(rx.State):
    params_data: Dict = {}

    def get_method(self):
        params = self.router.page.params
        self.params_data = params
