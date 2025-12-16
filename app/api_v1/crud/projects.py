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
from app.api_v1.schemas.project_schema import CreateProject
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
