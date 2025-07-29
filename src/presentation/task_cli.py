from src.domain.interfaces.task_service import TaskService

class TaskCLI:
    def __init__(self, task_service: TaskService):
        self.task_service = task_service

    def run(self):
        while True:
            print("\nTask Manager")
            print("1. Add Task")
            print("2. List Tasks")
            print("3. Update Task")
            print("4. Delete Task")
            print("5. Complete Task")
            print("6. Exit")
            
            choice = input("Select an option (1-6): ")
            print("")
            
            try:
                if choice == "1":
                    title = input("Enter task title: ")
                    description = input("Enter task description: ")
                    task = self.task_service.add_task(title, description)
                    print(f"Task added with ID: {task.id}")

                elif choice == "2":
                    tasks = self.task_service.list_tasks()
                    if not tasks:
                        print("No tasks found.")
                    for task in tasks:
                        status = "Completed" if task.completed else "Pending"
                        print(f"ID: {task.id}, Title: {task.title}, Status: {status}, Created: {task.created_at}")

                elif choice == "3":
                    task_id = int(input("Enter task ID to update: "))
                    title = input("Enter new title: ")
                    description = input("Enter new description: ")
                    if self.task_service.update_task(task_id, title, description):
                        print("Task updated successfully")
                    else:
                        print("Task not found")

                elif choice == "4":
                    task_id = int(input("Enter task ID to delete: "))
                    if self.task_service.delete_task(task_id):
                        print("Task deleted successfully")
                    else:
                        print("Task not found")

                elif choice == "5":
                    task_id = int(input("Enter task ID to complete: "))
                    if self.task_service.complete_task(task_id):
                        print("Task marked as completed")
                    else:
                        print("Task not found")

                elif choice == "6":
                    print("Exiting...")
                    break

                else:
                    print("Invalid option")

            except ValueError as e:
                print(f"Invalid input: {str(e)}")
            except Exception as e:
                print(f"An error occurred: {str(e)}")