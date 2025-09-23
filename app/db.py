from sqlmodel import SQLModel, Session, create_engine
from app.core.config import settings  
import os


DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:12345@localhost:5432/bookit")

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

def init_db():
    SQLModel.metadata.create_all(engine)
