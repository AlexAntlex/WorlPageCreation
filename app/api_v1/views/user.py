from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api_v1.crud import users as c_users
from app.core import db_helper
from app.api_v1.crud import users
from app.api_v1.schemas.user_schema import (
    UserCreate,
    UserBase,
    UserResponse,
    UserUpdate,
)
from app.api_v1.dependecies import user_by_id
from app.structure.models.user_model import User

router = APIRouter(prefix="/user", tags=["Users"])


@router.get("/", response_model=list[UserResponse])
async def get_users(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await users.get_users(session=session)


@router.post(
    "/add_user/", response_model=UserCreate, status_code=status.HTTP_201_CREATED
)
async def create_user(
    user_create: UserCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await users.create_user(session=session, user_create=user_create)


@router.get("/{user_id}/", response_model=UserBase)
async def get_one_user(
    user: User = Depends(user_by_id),
):
    return user


@router.patch("/update/{user_id}/")
async def update_user(
    user_update: UserUpdate,
    user: User = Depends(user_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await c_users.update_user(
        session=session,
        user=user,
        user_update=user_update,
    )


@router.delete("/delete/{user_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user: User = Depends(user_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    return await c_users.delete_user(session=session, user=user)
