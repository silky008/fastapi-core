from fastapi import FastAPI
from .routes import router
from .database import engine, Base

# This line **creates all tables** in the database
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)