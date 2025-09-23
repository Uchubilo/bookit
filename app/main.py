from fastapi import FastAPI
from app.routers import auth, users, services as services_router, bookings as bookings_router, reviews as reviews_router

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(services_router.router)
app.include_router(bookings_router.router)
app.include_router(reviews_router.router)
