from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Text
from app.core.database import Base
from app.structure.models.mixins import UserRelationMixin

if TYPE_CHECKING:
    from app.structure.models.comment_model import Comment


class Post(UserRelationMixin, Base):
    _user_back_populates = "posts"

    datatime: Mapped[str] = mapped_column(nullable=False)
    content_type: Mapped[str] = mapped_column(nullable=False)
    content_url: Mapped[str] = mapped_column(nullable=False)
    text: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default="",
        nullable=False,
    )

    comments: Mapped[list["Comment"]] = relationship(back_populates="post")
