from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api_v1.dependecies import project_by_id
from app.core import db_helper
from app.api_v1.crud import projects
from app.api_v1.schemas.project_schema import (
    ProjectBase,
    ProjectResponse,
    CreateProject,
    ProjectUpdate,
)
from app.structure.models.project_model import Project

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


@router.get("/project/{project_id}/", response_model=ProjectBase)
async def get_one_project(
    project: Project = Depends(project_by_id),
):
    return project


@router.patch("/update/{project_id}/")
async def update_project(
    project_update: ProjectUpdate,
    project: Project = Depends(project_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await projects.update_project(
        session=session,
        project=project,
        project_update=project_update,
    )


@router.delete("/delete/{project_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_project(
    project: Project = Depends(project_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    return await projects.delete_project(session=session, project=project)
