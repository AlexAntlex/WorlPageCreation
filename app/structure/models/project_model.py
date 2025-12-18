from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

if TYPE_CHECKING:
    from app.structure.models.user_model import User


class Project(Base):

    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    avatar: Mapped[str] = mapped_column(nullable=False)
    files_dir: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=datetime.now,
    )

    user: Mapped[list["User"]] = relationship(
        secondary="users_projects_association",
        back_populates="project",
    )
