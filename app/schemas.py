from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime

# -------- User --------
class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int
    is_active: bool
    class Config:
        orm_mode = True

# -------- Service --------
class ServiceBase(BaseModel):
    name: str
    description: str
    price: float

class ServiceCreate(ServiceBase):
    pass

class ServiceRead(ServiceBase):
    id: int
    class Config:
        orm_mode = True

# -------- Booking --------
class BookingCreate(BaseModel):
    service_id: int

class BookingRead(BaseModel):
    id: int
    user_id: int
    service_id: int
    booked_at: datetime
    class Config:
        orm_mode = True

# -------- Review --------
class ReviewCreate(BaseModel):
    service_id: int
    booking_id: int
    rating: int
    comment: str

class ReviewRead(ReviewCreate):
    id: int
    user_id: int
    created_at: datetime
    class Config:
        orm_mode = True

# -------- Auth / Token --------
class Token(BaseModel):
    access_token: str
    token_type: str
