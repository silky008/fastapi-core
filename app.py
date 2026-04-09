from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# User model
class User(BaseModel):
    id: int
    name: str
    email: str

# In-memory storage
users = []

# Create user
@app.post("/users/")
def create_user(user: User):
    users.append(user)
    return {"message": "User created", "user": user}

# Read all users
@app.get("/users/")
def get_users():
    return users

# Update user
@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: User):
    for index, user in enumerate(users):
        if user.id == user_id:
            users[index] = updated_user
            return {"message": "User updated", "user": updated_user}
    raise HTTPException(status_code=404, detail="User not found")

# Delete user
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user.id == user_id:
            users.pop(index)
            return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")