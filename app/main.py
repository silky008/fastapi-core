from fastapi import FastAPI

from .database import Base, engine
from .models import User
from .routes import router

app = FastAPI()

# IMPORTANT: create tables AFTER imports
Base.metadata.create_all(bind=engine)

app.include_router(router)