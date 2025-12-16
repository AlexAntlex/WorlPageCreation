from sqlalchemy import Text
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base
from app.structure.models.mixins import PostRelationMixin, UserRelationMixin


class Comment(UserRelationMixin, Base):
    _user_back_populates = "comments"
    _post_back_populates = "comments"

    text: Mapped[str] = mapped_column(Text, nullable=False)
    content_url: Mapped[str] = mapped_column(nullable=True)
