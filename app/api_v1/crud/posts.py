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
from app.api_v1.schemas.post_schema import CreatePost, UpdatePost
from app.structure.models.post_model import Post


async def create_post(session: AsyncSession, create_post: CreatePost) -> Post:
    post = Post(**create_post.model_dump())
    session.add(post)
    await session.commit()
    return post


# Добавить сортировку так же по id проекта
async def get_posts(session: AsyncSession) -> list[Post]:
    stmt = select(Post).order_by(Post.id)
    result: Result = await session.execute(stmt)
    posts = result.scalars().all()
    return list(posts)


async def get_one_post(session: AsyncSession, post_id: int) -> Post | None:
    return await session.get(Post, post_id)


async def update_post(
    session: AsyncSession, post: Post, post_update: UpdatePost
) -> Post:
    post_update.model_dump(exclude_unset=True)
    for name, value in post_update.model_dump().items():
        setattr(post, name, value)
    await session.commit()
    return post


async def delete_post(
    session: AsyncSession,
    post: Post,
) -> None:
    await session.delete(post)
