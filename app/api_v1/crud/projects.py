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
from app.api_v1.schemas.project_schema import CreateProject, ProjectUpdate
from app.structure.models.project_model import Project


async def create_project(
    session: AsyncSession, create_project: CreateProject
) -> Project:
    project = Project(**create_project.model_dump())
    session.add(project)
    await session.commit()
    return project


async def get_projects(session: AsyncSession) -> list[Project]:
    stmt = select(Project).order_by(Project.id)
    result: Result = await session.execute(stmt)
    projects = result.scalars().all()
    return list(projects)


async def get_one_project(session: AsyncSession, project_id: int) -> Project | None:
    return await session.get(Project, project_id)


async def update_project(
    session: AsyncSession, project: Project, project_update: ProjectUpdate
) -> Project:
    project_update.model_dump(exclude_unset=True)
    for name, value in project_update.model_dump().items():
        setattr(project, name, value)
    await session.commit()
    return project


async def delete_project(
    session: AsyncSession,
    project: Project,
) -> None:
    await session.delete(project)
