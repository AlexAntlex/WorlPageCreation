from abc import ABC, abstractmethod
from typing import Optional, List
from .entities import Comment


class ICommentRepository(ABC):

    @abstractmethod
    def create(self, comment: Comment) -> Comment:
        pass

    @abstractmethod
    def get(self, comment_id: int) -> Optional[Comment]:
        pass

    @abstractmethod
    def list(self) -> List[Comment]:
        pass
