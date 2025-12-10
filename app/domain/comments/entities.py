from dataclasses import dataclass
from typing import Optional


@dataclass
class Comment:
    id: int
    post_id: int
    author_id: int
    text: str
