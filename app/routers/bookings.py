from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlmodel import Session
from app.db import get_session
from app.models import Booking, User
from app.schemas import BookingCreate, BookingRead
from app.repositories import (
    create_booking_for_user,
    list_user_bookings,
    get_booking,
)
from app.core.security import get_current_user

router = APIRouter(prefix="/bookings", tags=["Bookings"])

@router.post("", response_model=BookingRead, status_code=status.HTTP_201_CREATED)
def create_booking(
    payload: BookingCreate,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    return create_booking_for_user(session, current_user.id, payload)

@router.get("", response_model=List[BookingRead])
def get_my_bookings(
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    return list_user_bookings(session, current_user.id)

@router.get("/{booking_id}", response_model=BookingRead)
def get_booking_by_id(
    booking_id: int,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    b = get_booking(session, booking_id)
    if not b:
        raise HTTPException(status_code=404, detail="Booking not found")
    if b.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not allowed")
    return b
