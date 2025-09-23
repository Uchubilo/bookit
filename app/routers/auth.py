from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from app.db import get_session
from app.schemas import UserCreate, Token
from app.services import register_user, authenticate_user, create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=Token)
def register(user: UserCreate, session: Session = Depends(get_session)):
    return register_user(session, user)

@router.post("/login", response_model=Token)
def login(user: UserCreate, session: Session = Depends(get_session)):
    return authenticate_user(session, user)
