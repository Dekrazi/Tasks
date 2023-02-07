import unittest
from model import Task
from controller import add_task, list_tasks

import unittest

class TestTasks(unittest.TestCase):
    def test_add_task(self):
        taskList = []
        add_task(taskList)

        self.assertEqual(len(taskList), 1)
        self.assertEqual(taskList[0].title, "TestT")
        self.assertEqual(taskList[0].desc, "TestD")
    
    def test_list_tasks(self):
        taskList = []
        list_tasks(taskList)
        taskList.append(Task('task1', 'desc1'))
        taskList.append(Task('task2', 'desc2'))

        self.assertEqual(len(taskList), 2)
        self.assertEqual(taskList[0].title, "task1")
        self.assertEqual(taskList[0].desc, "desc1")
        self.assertEqual(taskList[1].title, "task2")
        self.assertEqual(taskList[1].desc, "desc2")

if __name__ == '__main__':
    unittest.main()


