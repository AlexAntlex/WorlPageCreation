from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import db_helper
from app.api_v1.crud import projects
from app.api_v1.schemas.project_schema import (
    ProjectBase,
    ProjectResponse,
    CreateProject,
    UpdateProject,
)

router = APIRouter(prefix="/projects", tags=["Projects"])


@router.get("/", response_model=list[ProjectResponse])
async def get_projects(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await projects.get_projects(session=session)


@router.post("/add_project/", response_model=CreateProject)
async def create_project(
    create_project: CreateProject,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await projects.create_project(session=session, create_project=create_project)


@router.get("/{project_id}/", response_model=ProjectBase)
async def get_one_project(
    project_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    project = await projects.get_one_project(session=session, project_id=project_id)
    if project is not None:
        return project
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Project not found",
    )


@router.patch("/update/{project_id}/")
async def update_user(
    project_update: UpdateProject,
    project_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    get_pr = await projects.get_one_project(session=session, project_id=project_id)
    project = await projects.update_project(
        session=session, project_update=project_update, project=get_pr
    )
    if project is not None:
        return project
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Project not found",
    )


@router.delete("/delete/{project_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_project(
    project_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    project = await projects.get_one_project(session=session, project_id=project_id)
    return await projects.delete_project(session=session, project=project)
