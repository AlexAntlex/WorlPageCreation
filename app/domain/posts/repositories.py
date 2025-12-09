from abc import ABC, abstractmethod
from typing import Optional, List
from .entities import Post


class IPostRepository(ABC):

    @abstractmethod
    def create(self, post: Post) -> Post:
        pass

    @abstractmethod
    def get(self, post_id: int) -> Optional[Post]:
        pass

    @abstractmethod
    def list(self) -> List[Post]:
        pass
