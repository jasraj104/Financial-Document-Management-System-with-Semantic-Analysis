from fastapi import Depends
from jose import jwt
from sqlalchemy.orm import Session
from app.Database.db import get_db
from app.Database.models import User
from app.core.config import SECRET_KEY, ALGORITHM
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    username = payload.get("sub")

    user = db.query(User).filter(User.username == username).first()

    return user

from app.Database.models import Role, UserRole

def check_role(required_role: str):
    def role_checker(user=Depends(get_current_user), db: Session = Depends(get_db)):
        
        roles = db.query(Role).join(UserRole).filter(UserRole.user_id == user.id).all()

        role_names = [r.name for r in roles]

        if required_role not in role_names:
            raise Exception("Access denied")

        return user
    
    return role_checker

existing = db.query(User).filter(User.username == data.username).first()

if existing:
    raise HTTPException(status_code=400, detail="User already exists")