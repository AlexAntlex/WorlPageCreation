import uvicorn
from fastapi import FastAPI
from app.core.database import Base, engine
from app.ext_interdction.api import users

app = FastAPI(title="World Pages Creator")

# Создаём таблицы
Base.metadata.create_all(bind=engine)

# Роуты
app.include_router(users.router)


@app.get("/")
def index():
    return {"projects": {"progect_1", "progect_2", "progect_3", "progect_4"}}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
