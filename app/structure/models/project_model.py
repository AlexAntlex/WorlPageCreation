from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base


class Project(Base):

    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    # members: Mapped[List[int]] = mapped_column(nullable=True) Список участников
    # owner_id: Mapped[int] = mapped_column(nullable=False) id Создателя (отдельно от участников)
