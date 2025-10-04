# FastAPI E-commerce Backend

A FastAPI-based backend for an e-commerce platform providing **user authentication, account management, and product management APIs**.  
Supports JWT authentication, email verification, password reset, admin-only product management, and product search with filters.

---

## 🚀 Features

### Account / Authentication
- User registration & login
- JWT access & refresh token management (cookies)
- Email verification
- Password change & password reset via email
- Admin-only route access
- Logout with refresh token revocation

### Product Management
- Admin-only product creation
- List all products with pagination & optional category filtering
- Product search by title, description, categories, and price range
- Get product details by slug
- Upload product images

---

## 🛠️ Tech Stack

- **Framework:** FastAPI  
- **Database:** SQLAlchemy / PostgreSQL (`SessionDep`)  
- **Authentication:** JWT (access + refresh tokens)  
- **File Uploads:** FastAPI `UploadFile` for product images  
- **Environment Management:** `.env` for secret keys and token expiry

---

## 📦 Setup Instructions

### 1. Clone the repository
```bash
git clone git@github.com:ankitabelekar151/fastapi_ecommerce.git
cd fastapi_ecommerce

Create and activate virtual environment
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows


Install dependencies
pip install -r requirements.txt

Configure environment variables

Create a .env file in the root directory:

DATABASE_URL=postgresql://user:password@localhost/dbname
SECRET_KEY=your_secret_key
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7

Run the application
uvicorn main:app --reload

