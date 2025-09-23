from datetime import datetime, timedelta
from typing import Optional

from sqlmodel import Session, select
from passlib.context import CryptContext
from jose import jwt

from app.models import User, Service, Booking, Review

# ------------------ Security Setup ------------------ #
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "super-secret-key"        
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# ------------------ User Utilities ------------------ #
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# ------------------ User Services ------------------ #
def register_user(session: Session, email: str, password: str) -> User:
    """
    Create a new user with a hashed password.
    """
    # ensure email is unique
    existing = session.exec(select(User).where(User.email == email)).first()
    if existing:
        raise ValueError("Email already registered")

    user = User(email=email, hashed_password=hash_password(password))
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def authenticate_user(session: Session, email: str, password: str) -> Optional[User]:
    """
    Check if a user exists and the password is correct.
    """
    user = session.exec(select(User).where(User.email == email)).first()
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user

# ------------------ Service CRUD ------------------ #
def list_services(session: Session):
    """
    Return all available services.
    """
    return session.exec(select(Service)).all()

def get_service(session: Session, service_id: int) -> Optional[Service]:
    """
    Fetch a single service by ID.
    """
    return session.exec(select(Service).where(Service.id == service_id)).first()

def create_service(session: Session, name: str, description: str, price: float) -> Service:
    """
    Create a new service with basic details.
    """
    service = Service(name=name, description=description, price=price)
    session.add(service)
    session.commit()
    session.refresh(service)
    return service

# ------------------ Booking (optional demo) ------------------ #
def create_booking(session: Session, user_id: int, service_id: int) -> Booking:
    """
    Simple booking creation (example).
    """
    booking = Booking(user_id=user_id, service_id=service_id)
    session.add(booking)
    session.commit()
    session.refresh(booking)
    return booking

# ------------------ Review (optional demo) ------------------ #
def create_review(session: Session, user_id: int, booking_id: int, rating: int, comment: str) -> Review:
    """
    Create a review for a completed booking.
    """
    review = Review(user_id=user_id, booking_id=booking_id, rating=rating, comment=comment)
    session.add(review)
    session.commit()
    session.refresh(review)
    return review
