import unittest
from src.domain.entities.task import Task

class TestTask(unittest.TestCase):
    def test_task_creation(self):
        task = Task(1, "Test Task", "Description")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Description")
        self.assertFalse(task.completed)

    def test_task_to_dict(self):
        task = Task(1, "Test Task", "Description")
        task_dict = task.to_dict()
        self.assertEqual(task_dict["id"], 1)
        self.assertEqual(task_dict["title"], "Test Task")
        self.assertEqual(task_dict["description"], "Description")
        self.assertFalse(task_dict["completed"])

if __name__ == '__main__':
    unittest.main()