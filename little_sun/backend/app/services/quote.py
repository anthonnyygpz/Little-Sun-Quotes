from typing import Optional
from sqlalchemy.orm import Session

from little_sun.backend.app.crud.crud_quote_service import crud_quote_service
from little_sun.backend.app.crud.crud_quote_design import crud_quote_design
from little_sun.backend.app.crud.crud_quote import crud_quote
from little_sun.backend.app.crud.crud_client import crud_client
from little_sun.backend.app.models.client import Client
from little_sun.backend.app.schemas.client import ClientCreate
from little_sun.backend.app.schemas.quote_service import QuoteServiceCreate
from little_sun.backend.app.schemas.quote_design import QuoteDesignCreate
from little_sun.backend.app.schemas.quote import QuoteBase, QuoteCreate


class ServiceQuote:
    def check_if_client_exists(self, db: Session, *, name_in: str) -> Optional[Client]:
        return crud_client.get_by_name(db, name=name_in)

    def create_client(self, db: Session, *, obj_in: ClientCreate):
        return crud_client.create(db, obj_in=obj_in)

    def create_quote(self, db: Session, *, obj_in: QuoteCreate):
        return crud_quote.create(db, obj_in=obj_in)

    def create_quote_design(self, db: Session, obj_in: QuoteDesignCreate):
        return crud_quote_design.create(db, obj_in=obj_in)

    def create_quote_service(self, db: Session, *, obj_in: QuoteServiceCreate):
        return crud_quote_service.create(db, obj_in=obj_in)


service_quote = ServiceQuote()
