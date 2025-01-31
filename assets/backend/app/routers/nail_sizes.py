from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..dependencies import get_db
from ..services.nail_sizes import NailSizesRepositories

router = APIRouter(prefix="/api", tags=["Nail_services"], responses={400: {"description:": "Not found"}})

@router.get("/get_nail_sizes")
async def get_nail_sizes(db: Session = Depends(get_db)):
    return NailSizesRepositories(db).get_nail_sizes()
