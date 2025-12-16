from pydantic import BaseModel, ConfigDict


class ProjectBase(BaseModel):
    title: str
    description: str
    # owner_id: int
    # members: int


class CreateProject(ProjectBase):
    pass


class ProjectUpdate(CreateProject):
    title: str | None = None
    description: str | None = None


class ProjectResponse(ProjectBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
