from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import List
from app.db import get_session
from app.models import Service
from app.schemas import ServiceCreate, ServiceRead
from app.services import create_service, list_services, get_service

router = APIRouter(prefix="/services", tags=["Services"])

@router.get("", response_model=List[ServiceRead])
def get_all_services(session: Session = Depends(get_session)):
    return list_services(session)

@router.get("/{service_id}", response_model=ServiceRead)
def get_service_by_id(service_id: int, session: Session = Depends(get_session)):
    svc = get_service(session, service_id)
    if not svc:
        raise HTTPException(status_code=404, detail="Service not found")
    return svc

@router.post("", response_model=ServiceRead, status_code=status.HTTP_201_CREATED)
def create_new_service(payload: ServiceCreate, session: Session = Depends(get_session)):
    return create_service(session, payload.name, payload.description, payload.price)
