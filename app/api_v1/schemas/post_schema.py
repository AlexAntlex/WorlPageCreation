from pydantic import BaseModel, ConfigDict


class PostBase(BaseModel):

    # project_id: int
    author_id: int
    datatime: str
    content_type: str  # "photo", "video", "audio", "file", "text"
    content_url: str
    text: str


class CreatePost(PostBase):
    pass


class UpdatePost(CreatePost):

    content_url: str
    text: str


class PostResponse(PostBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
