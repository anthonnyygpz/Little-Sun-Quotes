from typing import Any, Dict, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from little_sun.backend.app.api import deps
from little_sun.backend.app.crud.crud_quote import crud_quote
from little_sun.backend.app.schemas.client import ClientCreate
from little_sun.backend.app.schemas.quote import (
    QuoteBase,
    QuoteCreate,
    QuoteResponse,
    QuoteUpdate,
)
from little_sun.backend.app.schemas.quote_design import QuoteDesignCreate
from little_sun.backend.app.schemas.quote_service import QuoteServiceCreate
from little_sun.backend.app.services.quote import service_quote

router = APIRouter()


@router.post("/create")
def create(quote_in: QuoteCreate, db: Session = Depends(deps.get_db)):
    return crud_quote.create(db, obj_in=quote_in)


@router.get("/all")
def get(db: Session = Depends(deps.get_db)) -> Any:
    return crud_quote.get_all(db)


@router.put("/update")
def update(quote_in: QuoteUpdate, db: Session = Depends(deps.get_db)) -> Any:
    return crud_quote.update(db, obj_in=quote_in)


@router.delete("/delete")
def delete(quote_id: int, db: Session = Depends(deps.get_db)) -> Any:
    return crud_quote.delete(db, id=quote_id)
