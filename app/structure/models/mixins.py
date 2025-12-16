from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import declared_attr, mapped_column, Mapped, relationship

if TYPE_CHECKING:
    from app.structure.models.user_model import User
    from app.structure.models.post_model import Post


class UserRelationMixin:
    _user_id_nullable: bool = False
    _user_id_unique: bool = False
    _user_back_populates: str | None = None

    @declared_attr
    def user_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey("users.id"),
            unique=cls._user_id_unique,
            nullable=cls._user_id_nullable,
        )

    @declared_attr
    def user(cls) -> Mapped["User"]:
        return relationship(
            "User",
            back_populates=cls._user_back_populates,
        )


class PostRelationMixin:
    _post_id_nullable: bool = False
    _post_id_unique: bool = False
    _post_back_populates: str | None = None

    @declared_attr
    def post_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey("posts.id"),
            unique=cls._post_id_unique,
            nullable=cls._post_id_nullable,
        )

    @declared_attr
    def post(cls) -> Mapped["Post"]:
        return relationship(
            "Post",
            back_populates=cls._post_back_populates,
        )
