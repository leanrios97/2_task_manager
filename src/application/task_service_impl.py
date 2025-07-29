from typing import List, Optional
from src.domain.entities.task import TaskEntity

from src.domain.interfaces.task_service import TaskService
from src.domain.interfaces.task_repository import TaskRepository

class TaskServiceImpl(TaskService):
    def __init__(self, repository: TaskRepository):
        self.repository = repository
        self.tasks = self.repository.load()

    def add_task(self, title: str, description: str) -> TaskEntity:
        task_id = max([task.id for task in self.tasks], default=0) + 1
        task = TaskEntity(task_id, title, description)
        self.tasks.append(task)
        self.repository.save(self.tasks)
        return task
    
    def get_task(self, task_id: int) -> Optional[TaskEntity]:
        return next((task for task in self.tasks if task.id == task_id), None)
    
    def update_task(self, task_id: int, title: str, description: str) -> bool:
        task = self.get_task(task_id)
        if task:
            task.title = title
            task.description = description
            self.repository.save(self.tasks)
            return True
        return False
    
    def delete_task(self, task_id: int) -> bool:
        task = self.get_task(task_id)
        if task:
            self.tasks = [t for t in self.tasks if t.id != task_id]
            self.repository.save(self.tasks)
            return True
        return False
    
    def complete_task(self, task_id: int) -> bool:
        task = self.get_task(task_id)
        if task:
            task.completed = True
            self.repository.save(self.tasks)
            return True
        return False

    def list_tasks(self) -> List[TaskEntity]:
        return self.tasks