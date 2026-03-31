from sqlalchemy.orm import Session
from app.Database.models import User
from app.core.security import hash_password, verify_password, create_access_token

def register_user(data, db: Session):
    user = User(
        username=data.username,
        email=data.email,
        password=hash_password(data.password)
    )
    db.add(user)
    db.commit()
    return user

def login_user(data, db: Session):
    user = db.query(User).filter(User.username == data.username).first()

    if not user or not verify_password(data.password, user.password):
        return None

    token = create_access_token({"sub": user.username})
    return token