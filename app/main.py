from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from app.core import Base, db_helper, config
from app.api_v1.crud import router as router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(title="World Pages Creator", lifespan=lifespan)
app.include_router(router=router)


@app.get("/")
def index():
    return {"projects": {"progect_1", "progect_2", "progect_3", "progect_4"}}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
