from sqlalchemy.orm import Session
from app.domain.users.entities import User
from app.domain.users.repositories import IUserRepository
from app.structure.models.user_model import UserModel


class UserRepository(IUserRepository):

    def __init__(self, db: Session):
        self.db = db

    def create(self, entity: User) -> User:
        model = UserModel(
            nickname=entity.nickname, bio=entity.bio, avatar_url=entity.avatar_url
        )
        self.db.add(model)
        self.db.commit()
        self.db.refresh(model)
        entity.id = model.id
        return entity

    def get(self, user_id: int) -> User | None:
        model = self.db.query(UserModel).get(user_id)
        if not model:
            return None
        return User(
            id=model.id,
            nickname=model.nickname,
            bio=model.bio,
            avatar_url=model.avatar_url,
            projects=[],
        )

    def list(self):
        models = self.db.query(UserModel).all()
        return [
            User(
                id=m.id,
                nickname=m.nickname,
                bio=m.bio,
                avatar_url=m.avatar_url,
                projects=[],
            )
            for m in models
        ]
