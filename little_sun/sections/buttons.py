import reflex as rx
from little_sun.components.buttons import (
    update_quote_button,
    generate_quote_button,
    clean_quote_button,
)
from little_sun.repositories.create_quotes import CreateQuotes
from little_sun.repositories.designs import DesignsState
from little_sun.repositories.info_client import ClientsState
from little_sun.repositories.nail_size import NailSizesState
from little_sun.repositories.params_url import ParamsUrl
from little_sun.repositories.services import ServicesState
from little_sun.repositories.status import StatusState
from little_sun.repositories.update_quote import UpdateQuote


def buttons():
    return rx.flex(
        # button generate quote
        rx.match(
            ParamsUrl.params_data["method"],
            (
                "PUT",
                update_quote_button(
                    state_update_quote=UpdateQuote,
                    form_data={
                        "quote_id": ParamsUrl.params_data["quote_id"],
                        "client_id": ParamsUrl.params_data["id_client"],
                        "nail_size_id": NailSizesState.size_id,
                        "name": ClientsState.name_client,
                        "phone_number": ClientsState.phone_number,
                        "total_amount": ServicesState.total_price,
                        "status": StatusState.status,
                        "services": ServicesState.service_selected,
                        "designs": DesignsState.design_selected,
                    },
                    url_redirect="http://localhost:3000/",
                ),
            ),
            (
                "POST",
                generate_quote_button(
                    state_state=CreateQuotes,
                    form_data={
                        "nail_size_id": NailSizesState.size_id,
                        "name": ClientsState.name_client,
                        "phone_number": ClientsState.phone_number,
                        "total_price_service": ServicesState.total_price,
                        "total_price_design": DesignsState.total_price,
                        "designs": DesignsState.design_selected,
                        "services": ServicesState.service_selected,
                    },
                    # url_redirect="http://localhost:3000/",
                ),
            ),
        ),
        # button clean all quotes
        clean_quote_button(),
        display="flex",
        justify_content="space-between",
    )
