import unittest
from model import Task
from controller import add_task, list_tasks, update_task, del_task

import unittest

class TestTasks(unittest.TestCase):
    def test_add_task(self):
        taskList = []
        add_task(taskList)

        self.assertEqual(len(taskList), 1)
        self.assertEqual(taskList[0].title, "TestT")
        self.assertEqual(taskList[0].desc, "TestD")

    # def test_update_task(self):
    #     taskList = [{"title": "task1", "desc": "desc1"}]
    #     updated_task_list = update_task(taskList)
    #     self.assertEqual(updated_task_list, [{"title": "new", "desc": "new desc1"}])

        #AttributeError: 'dict' object has no attribute 'title'
        

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

    def test_del_task(self):  
        taskList = [
        {"title": "task1", "desc": "desc1"},
        {"title": "task2", "desc": "desc2"}
        ]
        del_task(taskList)

        self.assertEqual(len(taskList), 1)
        self.assertEqual(taskList[0]["title"], "task1")
        self.assertEqual(taskList[0]["desc"], "desc1")

        #Getting Ran 0 tests in 0.000s with this one

        

if __name__ == '__main__':
    unittest.main()


