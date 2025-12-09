from typing import Annotated
from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.ext_interdction.schemas.user_schema import CreateUser, UserResponse
from app.domain.users.use_cases import CreateUser, GetUser
from app.structure.repositories.user_repo_impl import UserRepository

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/profile/add_user", response_model=UserResponse)
def create_user(body: CreateUser, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    uc = CreateUser(repo)
    user = uc.execute(
        nickname=body.nickname, email=email, bio=body.bio, avatar_url=body.avatar_url
    )
    return user


@router.get("/profile/{user_id}", response_model=UserResponse)
def get_user(user_id: Annotated[int, Path(ge=1)], db: Session = Depends(get_db)):
    repo = UserRepository(db)
    uc = GetUser(repo)
    return uc.execute(user_id)
