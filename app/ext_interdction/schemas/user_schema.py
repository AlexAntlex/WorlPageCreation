from pydantic import BaseModel, EmailStr
from typing import Optional


class CreateUser(BaseModel):
    nickname: str
    email: EmailStr
    bio: Optional[str] = None
    avatar_url: Optional[str] = None


class UserResponse(BaseModel):
    id: int
    nickname: str
    bio: Optional[str]
    avatar_url: Optional[str]
