from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import db_helper
from app.api_v1.crud import users
from app.api_v1.schemas.user_schema import UserCreate, UserBase, UserResponse

router = APIRouter(prefix="/profiles", tags=["Users"])


@router.get("/", response_model=list[UserResponse])
async def get_users(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await users.get_users(session=session)


@router.post("/add_user/", response_model=UserCreate)
async def create_user(
    user_create: UserCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await users.create_user(session=session, user_create=user_create)


@router.get("/user/{user_id}/", response_model=UserBase)
async def get_one_user(
    user_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    user = await users.get_one_user(session=session, user_id=user_id)
    if user is not None:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found",
    )
