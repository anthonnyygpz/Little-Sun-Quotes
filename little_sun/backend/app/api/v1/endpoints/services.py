from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from little_sun.backend.app.crud.crud_service import crud_service
from little_sun.backend.app.schemas.service import (
    ServiceCreate,
    ServiceResponse,
    ServiceUpdate,
)
from little_sun.backend.app.api import deps

router = APIRouter()


@router.post("/", response_model=ServiceResponse)
def create(service_in: ServiceCreate, db: Session = Depends(deps.get_db)) -> Any:
    service = crud_service.get_by_name(db, name_in=service_in.service_name)
    if service:
        raise HTTPException(status_code=404, detail="The Service not found")
    service = crud_service.create(db, obj_in=service_in)
    return service


@router.get("/", response_model=List[ServiceResponse])
def get_all(db: Session = Depends(deps.get_db)) -> Any:
    service = crud_service.get_all(db)
    if not service:
        raise HTTPException(status_code=404, detail="The Service not found")
    return service


@router.put("/{service_id}")
def update(service_in: ServiceUpdate, db: Session = Depends(deps.get_db)) -> Any:
    sculping_size = crud_service.update(db, obj_in=service_in)
    if not sculping_size:
        raise HTTPException(status_code=404, detail="The Service not found")
    return sculping_size


@router.delete("/{service_id}")
def delete(service_id: int, db: Session = Depends(deps.get_db)) -> Any:
    service = crud_service.get_by_id(db, service_id=service_id)
    if not service:
        raise HTTPException(status_code=404, detail="The Service not found")
    service = crud_service.delete(db, service_id=service_id)
    return service
