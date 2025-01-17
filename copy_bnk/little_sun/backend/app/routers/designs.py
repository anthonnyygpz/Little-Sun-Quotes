from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..dependencies import get_db
from ..services.design import DesignRepositories 


router = APIRouter(prefix="/api",tags=["Designs"], responses={400: {"description":"Not found"}})

@router.get("/get_design")
async def get_design(db: Session= Depends(get_db)):
   return  DesignRepositories(db).get_design_repositories()
