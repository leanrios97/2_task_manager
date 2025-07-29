from src.infrastructure.json_task_repository import JsonTaskRepository
from src.application.task_service_impl import TaskServiceImpl
from src.presentation.task_cli import TaskCLI

def main():
    repository = JsonTaskRepository()
    task_service = TaskServiceImpl(repository)
    cli = TaskCLI(task_service)
    cli.run()

if __name__ == "__main__":
    main()