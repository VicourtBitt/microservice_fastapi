from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Microservice"
    DATABASE_URL: str = ""
    PROJECT_VERSION: str = "0.1.0"
    SECRET_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()