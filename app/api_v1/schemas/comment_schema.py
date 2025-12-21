from pydantic import BaseModel, ConfigDict


class CommentBase(BaseModel):

    user_id: int
    created_at: str
    text: str
    content_url: str


class CreateComment(CommentBase):
    pass


class UpdateComment(CreateComment):

    text: str
    content_url: str


class CommentResponse(CommentBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
