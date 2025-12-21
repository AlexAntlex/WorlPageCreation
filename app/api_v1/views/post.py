from typing import Annotated

from fastapi import APIRouter, HTTPException, status, Depends, Path
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import db_helper
from app.api_v1.crud import posts
from app.api_v1.schemas.post_schema import (
    PostBase,
    PostResponse,
    CreatePost,
    UpdatePost,
)

router = APIRouter(prefix="/posts", tags=["Posts"])


@router.get("/", response_model=list[PostResponse])
async def get_posts(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await posts.get_posts(session=session)


@router.post("/add_post/", response_model=CreatePost)
async def create_post(
    create_post: CreatePost,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await posts.create_post(session=session, create_post=create_post)


@router.get("/{post_id}/", response_model=PostBase)
async def get_one_post(
    post_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    project = await posts.get_one_post(session=session, post_id=post_id)
    if project is not None:
        return project
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Project not found",
    )


@router.patch("/update/{post_id}/")
async def update_post(
    post_update: UpdatePost,
    post_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    get_pst = await posts.get_one_post(session=session, post_id=post_id)
    post = await posts.update_post(
        session=session, post_update=post_update, post=get_pst
    )
    if post is not None:
        return post
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Post not found",
    )


@router.delete("/delete/{post_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(
    post_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    post = await posts.get_one_post(session=session, post_id=post_id)
    return await posts.delete_post(session=session, post=post)
