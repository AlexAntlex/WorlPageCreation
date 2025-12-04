from pydantic import BaseModel
from typing import Optional

class UserCreateRequest(BaseModel):
    nickname: str
    bio: Optional[str] = None
    avatar_url: Optional[str] = None

class UserResponse(BaseModel):
    id: int
    nickname: str
    bio: Optional[str]
    avatar_url: Optional[str]
