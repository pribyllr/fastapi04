from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from models.base import Base

from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = "postgresql://{user}:{password}@{host}:{port}/fastapi_week4".format(
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()