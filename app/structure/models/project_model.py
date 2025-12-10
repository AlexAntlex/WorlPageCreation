from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base


class ProjectModel(Base):
    __tablename__ = "projects"

    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    # members: Mapped[str] = mapped_column(nullable=True)
    # owner_id: Mapped[int] = mapped_column(nullable=False)
