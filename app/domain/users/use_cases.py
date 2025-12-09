from .repositories import IUserRepository
from .entities import User

class CreateUser:
    def __init__(self, repo: IUserRepository):
        self.repo = repo

    def execute(self, nickname: str, bio: str = None, avatar_url: str = None) -> User:
        user = User(id=None, nickname=nickname, bio=bio, avatar_url=avatar_url)
        return self.repo.create(user)


class GetUser:
    def __init__(self, repo: IUserRepository):
        self.repo = repo

    def execute(self, user_id: int) -> User:
        return self.repo.get(user_id)
