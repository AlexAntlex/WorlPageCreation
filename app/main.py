from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from api_v1 import router as router_v1
from app.api_v1.crud import router as router
from app.api_v1.schemas.user_schema import UserCreate
from app.api_v1.views.user import create_user
from app.auth.crud import hash_password, authenticate_user, create_access_token
from app.auth.token_model import Token
from app.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(title="World Pages Creator", lifespan=lifespan)
app.include_router(router=router)
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)


@app.post("/register", status_code=201, summary="Create a new user")
def register_user(body: UserCreate):
    hashed = hash_password(body.password)
    create_user(body.username, hashed, body.full_name or "")
    return {"message": "User registered successfully"}


@app.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token({"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/me", response_model=UserPublic, summary="Get my profile (protected)")
def read_me(current_user: User = Depends(get_current_user)):
    return current_user


@app.get("/")
def index():
    return {"projects": {"progect_1", "progect_2", "progect_3", "progect_4"}}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
