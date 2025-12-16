import os
from pydantic import BaseModel
from pydantic_settings import BaseSettings

# BASE_DIR = Path(__file__).resolve().parent -> не работает с папкой data
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


class DBSettings(BaseModel):
    db_url: str = f"sqlite+aiosqlite:///{BASE_DIR}/data/app.sqlite3"
    db_echo: bool = True


class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    db: DBSettings = DBSettings()


settings = Settings()
