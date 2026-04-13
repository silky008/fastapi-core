from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from .security  import hash_password, create_access_token, verify_password
from .models import User
from .schemas import UserCreate, UserRead
from .database import get_db

router = APIRouter()

# Create user
@router.post("/users/", response_model=UserRead)
def create_user(user: UserCreate, db:Session = Depends(get_db)):
    print("CREATE USER FUNCTION CALLED")
    db_user = User(name=user.name, email=user.email,password=hash_password(user.password))
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
   
    return db_user

# Get all users
@router.get("/users/", response_model=list[UserRead])
def get_users(db:Session = Depends(get_db)):
    users = db.query(User).all()
    return users

# Update user
@router.put("/users/{user_id}", response_model=UserRead)
def update_user(user_id: int, updated_user: UserCreate,db:Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.name = updated_user.name
    db_user.email = updated_user.email
    db.commit()
    db.refresh(db_user)
    return db_user

# Delete user
@router.delete("/users/{user_id}")
def delete_user(user_id: int,db:Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        db.close()
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted"}

@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.email})
    return {"access_token": token}