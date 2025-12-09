from dataclasses import dataclass
from pydantic import EmailStr
from typing import Optional, List


@dataclass
class User:
    id: Optional[int]
    email: EmailStr
    nickname: str
    bio: Optional[str]
    avatar_url: Optional[str]
    projects: List[int] = None  # id проектов
