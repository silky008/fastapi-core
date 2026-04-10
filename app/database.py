from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root:root@localhost/fastapi_users"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

def get_db():
    db:Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    