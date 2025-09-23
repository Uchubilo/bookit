from typing import List, Optional
from sqlmodel import Session, select
from datetime import datetime
from app.models import User, Service, Booking, Review
from app.schemas import BookingCreate, ReviewCreate, ServiceCreate

# -------- Service --------
def create_service(session: Session, payload: ServiceCreate) -> Service:
    service = Service(**payload.dict())
    session.add(service)
    session.commit()
    session.refresh(service)
    return service

def list_services(session: Session) -> List[Service]:
    return session.exec(select(Service)).all()

def get_service(session: Session, service_id: int) -> Optional[Service]:
    return session.get(Service, service_id)

# -------- Booking --------
def create_booking_for_user(session: Session, user_id: int, payload: BookingCreate) -> Booking:
    booking = Booking(user_id=user_id, **payload.dict())
    session.add(booking)
    session.commit()
    session.refresh(booking)
    return booking

def list_user_bookings(session: Session, user_id: int) -> List[Booking]:
    return session.exec(select(Booking).where(Booking.user_id == user_id)).all()

def get_booking(session: Session, booking_id: int) -> Optional[Booking]:
    return session.get(Booking, booking_id)

# -------- Review --------
def create_review_for_booking(session: Session, user_id: int, payload: ReviewCreate) -> Review:
    review = Review(user_id=user_id, **payload.dict())
    session.add(review)
    session.commit()
    session.refresh(review)
    return review

def get_reviews_by_service(session: Session, service_id: int) -> List[Review]:
    return session.exec(select(Review).where(Review.service_id == service_id)).all()

def get_review(session: Session, review_id: int) -> Optional[Review]:
    return session.get(Review, review_id)
