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
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days
    SECRET_KEY: str = os.environ["JWT_SECRET_KEY"]  # should be kept secret
    REFRESH_SECRET_KEY: str = os.environ["JWT_REFRESH_SECRET_KEY"]


settings = Settings()
