import httpx
import reflex as rx


class DeleteQuote(rx.State):
    success: str = ""

    @rx.event
    async def delete_quote(self, quote_id: int):
        try:
            async with httpx.AsyncClient() as client:
                respose = await client.delete(
                    f"http://0.0.0.0:8000/api_v1/quotes/delete?quote_id={quote_id}"
                )
                if respose:
                    self.success = "Se borro correctamente"
        except httpx.HTTPError as e:
            self.success = f"Error HTTP: {e}"
            raise
        except Exception as e:
            self.success = f"Error inesperado: {e}"
            raise
