from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from little_sun.backend.app.services.nail_services import (
    NailServicesRepositories,
)
from ..dependencies import get_db

router = APIRouter(
    prefix="/api",
    tags=["Nail_service"],
    responses={400: {"description": "Not found"}},
)


@router.get("/get_nail_services")
async def get_nail_services(db: Session = Depends(get_db)):
    return NailServicesRepositories(db).get_nail_services_repositories()
