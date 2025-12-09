from abc import ABC, abstractmethod
from typing import Optional, List
from .entities import Project


class IProjectRepository(ABC):

    @abstractmethod
    def create(self, project: Project) -> Project:
        pass

    @abstractmethod
    def get(self, project_id: int) -> Optional[Project]:
        pass

    @abstractmethod
    def list(self) -> List[Project]:
        pass
