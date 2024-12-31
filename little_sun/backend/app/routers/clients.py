from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from little_sun.backend.app.schemas.client import CreateClientsSchema
from ..dependencies import get_db
from ..services.clients import ClientsRepositories

router = APIRouter(
    prefix="/api",
    tags=["Clients"],
    responses={400: {"description": "Not found"}},
)


@router.post("/register_clients")
async def register_clients(
    client: CreateClientsSchema, db: Session = Depends(get_db)
):
    return ClientsRepositories(db).register_clients_repositories(client)


@router.get("/get_clients")
async def get_clients(db: Session = Depends(get_db)):
    return ClientsRepositories(db).get_clients_repositories()


@router.get("/get_one_clients")
async def get_one_clients(name: str, db: Session = Depends(get_db)):
    return ClientsRepositories(db).get_one_client_repositories(name)
