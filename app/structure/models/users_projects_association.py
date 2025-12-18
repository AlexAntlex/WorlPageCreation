from sqlalchemy import Table, Column, ForeignKey, Integer, UniqueConstraint, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core import Base


class UserProjectAssociation(Base):
    __tablename__ = "user_projects_association"
    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "project_id",
            name="uniq_users_projects_idx",
        ),
    )
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id"))

    role: Mapped[str] = mapped_column(
        String, nullable=False, default="watcher", server_default="watcher"
    )
