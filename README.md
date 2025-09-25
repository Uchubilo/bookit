# Bookit

Bookit is a **FastAPI + SQLModel** application for booking services, managing users, and collecting reviews.  
It provides a clean REST API with JWT authentication.

---
STRUCTURE
bookit/
│
├─ app/
│   ├─ __init__.py
│   ├─ main.py
│   ├─ db.py
│   ├─ models.py
│   ├─ schemas.py
│   ├─ services.py
│   ├─ repositories.py
│   ├─ core/
│   │   └─ ...
│   └─ routers/
│       ├─ __init__.py
│       ├─ auth.py
│       ├─ bookings.py
│       ├─ reviews.py
│       ├─ services.py
│       └─ users.py


## 🚀 Features

- **User Registration & Login** (JWT auth)
- **Service Management** (CRUD)
- **Bookings & Reviews**
- PostgreSQL database with Alembic migrations
- Docker support (optional)

---

## 🏗️ Tech Stack

- **FastAPI** – High-performance Python web framework
- **SQLModel** – ORM for models + queries
- **PostgreSQL** – Database
- **Alembic** – Migrations
- **Docker** – Containerization (optional)

---

## ⚡ Local Development

### Prerequisites

- Python **3.11+**
- PostgreSQL installed and running  
  Create a database:
  ```bash
  createdb bookit
  ```

1. Clone & Setup
   git clone https://github.com/<your-username>/bookit.git
   cd bookit
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
   pip install -r requirements.txt

2. Environment Variables

Create a .env file in the root directory:

DATABASE_URL=postgresql://postgres:postgres@localhost:5432/bookit
SECRET_KEY=your-secret-key
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7

3. Apply Database Migrations
   alembic upgrade head

4. Start the Server
   uvicorn app.main:app --reload

5. Test the API

Open your browser at:

http://127.0.0.1:8000/docs

This opens the interactive Swagger UI.

Robust, ACID-compliant, open-source
Strong support for JSON, constraints, and indexing
Ideal for relational data (users, bookings, reviews)
Mature Alembic integration for migrations
Preferred in production over SQLite/MySQL for reliability and features
