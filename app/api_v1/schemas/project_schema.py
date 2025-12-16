from pydantic import BaseModel, EmailStr, ConfigDict


class ProjectBase(BaseModel):
    title: str
    description: str
    # owner_id: int
    # members: int


class CreateProject(ProjectBase):
    pass


class UpdateProject(CreateProject):
    description: str = str | None


class ProjectResponse(ProjectBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
