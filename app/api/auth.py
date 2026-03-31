from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserRegister, UserLogin
from app.services.auth_service import register_user, login_user
from app.Database.db import get_db
from fastapi import HTTPException


router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
def register(data: UserRegister, db: Session = Depends(get_db)):
    try:
        print("Incoming data:", data)

        register_user(data, db)

        return {"message": "User registered"}
    
    except Exception as e:
        print("ERROR:", e)   # 🔥 THIS WILL SHOW REAL ERROR
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/login")
def login(data: UserLogin, db: Session = Depends(get_db)):
    token = login_user(data, db)

    if not token:
        return {"error": "Invalid credentials"}

    return {"access_token": token}