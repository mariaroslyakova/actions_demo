# tests/test_taskclass.py
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from TaskClass import Task, TaskManager
import unittest


class TestTask(unittest.TestCase):
    def test_task_creation(self):
        task = Task("Test Task", "Test Description")
        self.assertEqual(task.title, "Test Task")
        self.assertEqual(task.description, "Test Description")
        self.assertFalse(task.is_completed)
    
    def test_task_mark_completed(self):
        task = Task("Test Task")
        task.mark_as_completed()
        self.assertTrue(task.is_completed)
    
    def test_task_mark_incomplete(self):
        task = Task("Test Task", is_completed=True)
        task.mark_as_incomplete()
        self.assertFalse(task.is_completed)
    
    def test_task_update(self):
        task = Task("Old Title", "Old Description")
        task.update_title("New Title").update_description("New Description")
        self.assertEqual(task.title, "New Title")
        self.assertEqual(task.description, "New Description")
    
    def test_task_str_representation(self):
        task = Task("Test Task")
        self.assertIn("Test Task", str(task))
    
    def test_task_to_dict(self):
        task = Task("Test", "Desc", True)
        task_dict = task.to_dict()
        self.assertEqual(task_dict['title'], "Test")
        self.assertEqual(task_dict['description'], "Desc")
        self.assertTrue(task_dict['is_completed'])


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()
        self.task1 = Task("Task 1")
        self.task2 = Task("Task 2", is_completed=True)
    
    def test_add_task(self):
        self.manager.add_task(self.task1)
        self.assertEqual(len(self.manager), 1)
    
    def test_remove_task(self):
        self.manager.add_task(self.task1).add_task(self.task2)
        self.manager.remove_task("Task 1")
        self.assertEqual(len(self.manager), 1)
        self.assertEqual(self.manager.tasks[0].title, "Task 2")
    
    def test_get_task(self):
        self.manager.add_task(self.task1)
        found = self.manager.get_task("Task 1")
        self.assertIsNotNone(found)
        self.assertEqual(found.title, "Task 1")
    
    def test_get_completed_tasks(self):
        self.manager.add_task(self.task1).add_task(self.task2)
        completed = self.manager.get_completed_tasks()
        self.assertEqual(len(completed), 1)
        self.assertEqual(completed[0].title, "Task 2")
    
    def test_get_incomplete_tasks(self):
        self.manager.add_task(self.task1).add_task(self.task2)
        incomplete = self.manager.get_incomplete_tasks()
        self.assertEqual(len(incomplete), 1)
        self.assertEqual(incomplete[0].title, "Task 1")
    
    def test_clear_all_tasks(self):
        self.manager.add_task(self.task1).add_task(self.task2)
        self.manager.clear_all_tasks()
        self.assertEqual(len(self.manager), 0)
    
    def test_iteration(self):
        self.manager.add_task(self.task1).add_task(self.task2)
        tasks = list(self.manager)
        self.assertEqual(len(tasks), 2)


if name == '__main__':
    unittest.main()
