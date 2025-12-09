from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base


class UserModel(Base):
    __tablename__ = "users"

    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    bio: Mapped[str] = mapped_column(nullable=True)
    avatar_url: Mapped[str] = mapped_column(nullable=True)
