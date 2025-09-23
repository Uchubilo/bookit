from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlmodel import Session
from app.db import get_session
from app.models import Review, User
from app.schemas import ReviewCreate, ReviewRead
from app.repositories import (
    create_review_for_booking,
    get_reviews_by_service,
    get_review,
    get_booking
)
from app.core.security import get_current_user

router = APIRouter(prefix="/reviews", tags=["Reviews"])

@router.post("", response_model=ReviewRead, status_code=status.HTTP_201_CREATED)
def post_review(
    payload: ReviewCreate,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    return create_review_for_booking(session, current_user.id, payload)

@router.get("/service/{service_id}", response_model=List[ReviewRead])
def get_service_reviews(service_id: int, session: Session = Depends(get_session)):
    return get_reviews_by_service(session, service_id)

@router.delete("/{review_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_review(
    review_id: int,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    r = get_review(session, review_id)
    if not r:
        raise HTTPException(status_code=404, detail="Review not found")
    b = get_booking(session, r.booking_id)
    if current_user.id != b.user_id:
        raise HTTPException(status_code=403, detail="Not allowed")
    session.delete(r)
    session.commit()
    return
