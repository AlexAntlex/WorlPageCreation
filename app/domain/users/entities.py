from dataclasses import dataclass
from typing import Optional, List

@dataclass
class User:
    id: Optional[int]
    nickname: str
    bio: Optional[str]
    avatar_url: Optional[str]
    projects: List[int] = None  # id проектов
