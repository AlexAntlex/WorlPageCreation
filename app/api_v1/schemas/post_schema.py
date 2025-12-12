from pydantic import BaseModel, EmailStr, ConfigDict


class PostBase(BaseModel):
    id: int
    project_id: int
    author_id: int
    datatime: str
    content_type: str  # "photo", "video", "audio", "file", "text"
    content_url: str
    text: str


class CreatePost(PostBase):
    pass


class PostResponse(PostBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
