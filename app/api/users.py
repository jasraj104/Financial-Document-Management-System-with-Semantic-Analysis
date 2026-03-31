from app.Database.models import Role
from app.Database.db import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi import APIRouter

router = APIRouter()

@router.post("/roles/create")
def create_role(name: str, db: Session = Depends(get_db)):
    role = Role(name=name)
    db.add(role)
    db.commit()
    return {"message": "Role created"}

from app.Database.models import UserRole

@router.post("/assign-role")
def assign_role(user_id: int, role_id: int, db: Session = Depends(get_db)):
    
    mapping = UserRole(user_id=user_id, role_id=role_id)
    db.add(mapping)
    db.commit()

    return {"message": "Role assigned"}

@router.get("/{user_id}/roles")
def get_roles(user_id: int, db: Session = Depends(get_db)):
    
    roles = db.query(Role).join(UserRole).filter(UserRole.user_id == user_id).all()

    return {"roles": [r.name for r in roles]}

@router.get("/{user_id}/permissions")
def get_permissions(user_id: int, db: Session = Depends(get_db)):

    roles = db.query(Role).join(UserRole).filter(UserRole.user_id == user_id).all()

    permissions_map = {
        "Admin": ["full_access"],
        "Analyst": ["upload", "edit"],
        "Auditor": ["review"],
        "Client": ["view"]
    }

    permissions = []
    for role in roles:
        permissions.extend(permissions_map.get(role.name, []))

    return {"permissions": permissions}