from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base


class PostModel(Base):
    __tablename__ = "posts"

    datatime: Mapped[str] = mapped_column(nullable=False)
    content_type: Mapped[str] = mapped_column(nullable=False)
    content_url: Mapped[str] = mapped_column(nullable=False)
    text: Mapped[str] = mapped_column(nullable=False)
    # project_id: Mapped[int] = mapped_column(nullable=False)
    # author_id: Mapped[int] = mapped_column(nullable=False)
