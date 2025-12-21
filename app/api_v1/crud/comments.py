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
from app.api_v1.schemas.comment_schema import CreateComment, UpdateComment
from app.structure.models.comment_model import Comment


async def create_comment(
    session: AsyncSession, create_comment: CreateComment
) -> Comment:
    comment = Comment(**create_comment.model_dump())
    session.add(comment)
    await session.commit()
    return comment


async def get_comments(session: AsyncSession) -> list[Comment]:
    stmt = select(Comment).order_by(Comment.id)
    result: Result = await session.execute(stmt)
    comments = result.scalars().all()
    return list(comments)


async def get_one_comment(session: AsyncSession, comment_id: int) -> Comment | None:
    return await session.get(Comment, comment_id)


async def update_comment(
    session: AsyncSession, comment: Comment, comment_update: UpdateComment
) -> Comment:
    comment_update.model_dump(exclude_unset=True)
    for name, value in comment_update.model_dump().items():
        setattr(comment, name, value)
    await session.commit()
    return comment


async def delete_comment(
    session: AsyncSession,
    comment: Comment,
) -> None:
    await session.delete(comment)
