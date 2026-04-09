from fastapi import APIRouter, HTTPException
from .models import User

router = APIRouter()

users = []

@router.post("/users/")
def create_user(user: User):
    users.append(user)
    return {"message": "User created", "user": user}

@router.get("/users/")
def get_users():
    return users

@router.put("/users/{user_id}")
def update_user(user_id: int, updated_user: User):
    for index, user in enumerate(users):
        if user.id == user_id:
            users[index] = updated_user
            return {"message": "User updated", "user": updated_user}
    raise HTTPException(status_code=404, detail="User not found")

@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user.id == user_id:
            users.pop(index)
            return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")