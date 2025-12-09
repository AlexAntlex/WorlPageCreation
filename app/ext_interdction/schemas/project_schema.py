from pydantic import BaseModel, EmailStr
from typing import Optional
from app.domain.users.entities import User


class CreateProject(BaseModel):
    name: str
    author: User
    bio: Optional[str] = None
    avatar_url: Optional[str] = None


class ProjectResponse(BaseModel):
    id: int
    name: str
    author: User
    bio: Optional[str]
    avatar_url: Optional[str]
