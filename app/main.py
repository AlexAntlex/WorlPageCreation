from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from api_v1 import router as router_v1
from app.api_v1.crud import router as router
from app.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(title="World Pages Creator", lifespan=lifespan)
app.include_router(router=router)
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)


@app.get("/")
def index():
    return {"projects": {"progect_1", "progect_2", "progect_3", "progect_4"}}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
