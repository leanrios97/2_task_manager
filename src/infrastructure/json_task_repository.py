import json
import os
from typing import List
from src.domain.entities.task import TaskEntity
from src.domain.interfaces.task_repository import TaskRepository

class JsonTaskRepository(TaskRepository):
    def __init__(self, file_path: str = "data/tasks.json"):
        self.file_path = file_path

    def save(self, tasks: List[TaskEntity]) -> None:
        try:
            with open(self.file_path, 'w') as file:
                json.dump([task.to_dict() for task in tasks], file, indent=2)
        except IOError as e:
            raise Exception(f"Error saving tasks: {str(e)}")

    def load(self) -> List[TaskEntity]:
        try:
            if not os.path.exists(self.file_path):
                return []
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                return [TaskEntity(**task) for task in data]
        except (IOError, json.JSONDecodeError) as e:
            raise Exception(f"Error loading tasks: {str(e)}")