from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.db import get_session
from app.models import User
from app.core.security import get_current_user  

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/me")
def read_current_user(current_user: User = Depends(get_current_user)):
    """
    Return the authenticated user's details.
    """
    return current_user
