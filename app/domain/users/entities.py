from dataclasses import dataclass
from pydantic import EmailStr
from typing import Optional, List


@dataclass
class User:
    id: int
    email: EmailStr
    name: str
    bio: Optional[str]
    avatar_url: Optional[str]
    projects: List[int] = None  # id проектов
