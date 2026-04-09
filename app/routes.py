from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from .models import User
from .schemas import UserCreate, UserRead
from .database import SessionLocal

router = APIRouter()

# Create user
@router.post("/users/", response_model=UserRead)
def create_user(user: UserCreate):
    db: Session = SessionLocal()
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db.close()
    return db_user

# Get all users
@router.get("/users/", response_model=list[UserRead])
def get_users():
    db: Session = SessionLocal()
    users = db.query(User).all()
    db.close()
    return users

# Update user
@router.put("/users/{user_id}", response_model=UserRead)
def update_user(user_id: int, updated_user: UserCreate):
    db: Session = SessionLocal()
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        db.close()
        raise HTTPException(status_code=404, detail="User not found")
    db_user.name = updated_user.name
    db_user.email = updated_user.email
    db.commit()
    db.refresh(db_user)
    db.close()
    return db_user

# Delete user
@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    db: Session = SessionLocal()
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        db.close()
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    db.close()
    return {"message": "User deleted"}