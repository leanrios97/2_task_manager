from abc import ABC, abstractmethod
from typing import List
from src.domain.entities.task import TaskEntity

class TaskRepository(ABC):
    @abstractmethod 
    def save(self, task: List[TaskEntity]) -> None:
        """Save a task entity to the repository."""
        pass

    @abstractmethod
    def load(self) -> List[TaskEntity]:
        """Load a task entity from the repository by its ID."""
        pass