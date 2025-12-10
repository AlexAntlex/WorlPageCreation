from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Post:
    id: int
    project_id: int
    author_id: int
    content_type: str  # "photo", "video", "audio", "file", "text"
    content_url: Optional[str]
    text: Optional[str]
