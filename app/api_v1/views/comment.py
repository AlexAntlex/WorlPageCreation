from typing import Annotated

from fastapi import APIRouter, HTTPException, status, Depends, Path
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import db_helper
from app.api_v1.crud import comments
from app.api_v1.schemas.comment_schema import (
    CommentResponse,
    CommentBase,
    CreateComment,
    UpdateComment,
)

router = APIRouter(prefix="/comment", tags=["Comments"])


@router.get("/", response_model=list[CommentResponse])
async def get_comments(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await comments.get_comments(session=session)


@router.post("/add_comment/", response_model=CreateComment)
async def create_comment(
    create_comment: CreateComment,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await comments.create_comment(session=session, create_comment=create_comment)


@router.get("/{comment_id}/", response_model=CommentBase)
async def get_one_comment(
    comment_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    comment = await comments.get_one_comment(session=session, comment_id=comment_id)
    if comment is not None:
        return comment
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Comment not found",
    )


@router.patch("/update/{comment_id}/")
async def update_comment(
    comment_update: UpdateComment,
    comment_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    get_cm = await comments.get_one_comment(session=session, comment_id=comment_id)
    comment = await comments.update_comment(
        session=session, comment_update=comment_update, comment=get_cm
    )
    if comment is not None:
        return comment
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Comment not found",
    )


@router.delete("/delete/{comment_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_comment(
    comment_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    comment = await comments.get_one_project(session=session, comment_id=comment_id)
    return await comments.delete_project(session=session, comment=comment)
