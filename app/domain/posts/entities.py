from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Post:
    id: int
    project_id: int
    author_id: int
    datatime: str
    content_type: List[str]  # "photo", "video", "audio", "file", "text"
    content_url: Optional[str]
    text: Optional[str]
