"""
CRUD

Create
Read
Update
Delete

"""

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from app.api_v1.schemas.user_schema import UserCreate
from app.structure.models.user_model import UserModel


async def create_user(session: AsyncSession, user_create: UserCreate) -> UserModel:
    user = UserModel(**user_create.model_dump())
    session.add(user)
    await session.commit()
    return user


async def get_users(session: AsyncSession) -> list[UserModel]:
    stmt = select(UserModel).order_by(UserModel.id)
    result: Result = await session.execute(stmt)
    users = result.scalars().all()
    return list(users)


async def get_one_user(session: AsyncSession, user_id: int) -> UserModel | None:
    return await session.get(UserModel, user_id)
