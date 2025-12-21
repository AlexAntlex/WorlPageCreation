from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base

if TYPE_CHECKING:
    from app.structure.models.post_model import Post
    from app.structure.models.comment_model import Comment
    from app.structure.models.project_model import Project


class User(Base):

    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    bio: Mapped[str] = mapped_column(nullable=True)
    avatar_url: Mapped[str] = mapped_column(nullable=True)
    hashed_password: Mapped[str] = mapped_column(nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.now,
    )

    posts: Mapped[list["Post"]] = relationship(
        back_populates="user",
    )

    comments: Mapped[list["Comment"]] = relationship(
        back_populates="user",
    )

    projects: Mapped[list["Project"]] = relationship(
        secondary="users_projects_association",
        back_populates="user",
    )
