from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str

class UserRead(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True #tells Pydantic it can read SQLAlchemy objects directly. This prevents the create_model_field error.