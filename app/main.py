from fastapi import FastAPI
from app.core.database import Base, engine
from app.presentation.api import users

app = FastAPI(title="Projects Platform")

# Создаём таблицы
Base.metadata.create_all(bind=engine)

# Роуты
app.include_router(users.router)
