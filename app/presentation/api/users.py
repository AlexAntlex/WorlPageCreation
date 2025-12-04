from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.presentation.schemas.user_schema import UserCreateRequest, UserResponse
from app.domain.users.use_cases import CreateUser, GetUser
from app.infrastructure.repositories.user_repo_impl import UserRepository

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse)
def create_user(body: UserCreateRequest, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    uc = CreateUser(repo)
    user = uc.execute(
        nickname=body.nickname,
        bio=body.bio,
        avatar_url=body.avatar_url
    )
    return user

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    uc = GetUser(repo)
    return uc.execute(user_id)
