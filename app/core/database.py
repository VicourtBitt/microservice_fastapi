from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
import os

## Load environment variables
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

## Database URL
DATABASE_URL = os.getenv("DB_URI", f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

## Create engine
engine = create_engine(DATABASE_URL)

def get_db() -> Session:
    with Session(engine) as session:
        yield session