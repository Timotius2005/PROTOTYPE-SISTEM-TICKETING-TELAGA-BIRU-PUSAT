import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
load_dotenv()
class Settings(BaseSettings):

    DATABASE_URL: str = os.getenv("DATABASE_URL")
    PROJECT_NAME: str = "Sistem Pusat Tiket"
    VERSION: str = "1.0.0"
    class Config:
        case_sensitive = True

settings = Settings()
