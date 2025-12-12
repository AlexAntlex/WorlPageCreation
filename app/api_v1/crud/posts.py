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
from app.api_v1.schemas.post_schema import CreatePost
from app.structure.models.post_model import PostModel


async def create_post(session: AsyncSession, create_post: CreatePost) -> PostModel:
    post = PostModel(**create_post.model_dump())
    session.add(post)
    await session.commit()
    return post


# Добавить сортировку так же по id проекта
async def get_posts(session: AsyncSession) -> list[PostModel]:
    stmt = select(PostModel).order_by(PostModel.id)
    result: Result = await session.execute(stmt)
    posts = result.scalars().all()
    return list(posts)


async def get_one_post(session: AsyncSession, post_id: int) -> PostModel | None:
    return await session.get(PostModel, post_id)
