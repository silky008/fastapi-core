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