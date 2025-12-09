from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Project:
    id: Optional[int]
    title: str
    description: Optional[str]
    owner_id: int
    members: List[int]
