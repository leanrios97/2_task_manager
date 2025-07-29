from abc import ABC, abstractmethod
from typing import List, Optional
from src.domain.entities.task import TaskEntity

class TaskService(ABC):
    @abstractmethod
    def add_task(self, title: str, description: str) -> TaskEntity:
        """Add a new task to the service."""
        pass

    @abstractmethod
    def get_task(self, task_id: int) -> Optional[TaskEntity]:
        """Get a task by its ID."""
        pass

    @abstractmethod
    def update_task(self, task_id: int, title: str, description: str) -> bool:
        """Update an existing task."""
        pass

    @abstractmethod
    def delete_task(self, task_id: int) -> bool:
        """Delete a task by its ID."""
        pass

    @abstractmethod
    def complete_task(self, task_id: int) -> bool:
        """Mark a task as completed."""
        pass

    @abstractmethod
    def list_tasks(self) -> List[TaskEntity]:
        """List all tasks."""
        pass

