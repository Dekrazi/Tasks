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

        
    def test_add_task(self):
        taskList = []
        add_task(taskList)

        self.assertEqual(len(taskList), 1)
        self.assertEqual(taskList[0].title, "new title")
        self.assertEqual(taskList[0].desc, "new desc")

    def test_update_task_by_index(self):
        task_list = [Task("Clean the House", "Wipe down counters"),
                    Task("Grocery Store", "Buy bread")]
        #Assuming user wants to update task with index[0]
        updated_task_list = update_task(task_list)
        self.assertEqual(updated_task_list[0].title, "updated title")
        self.assertEqual(updated_task_list[0].desc, "updated desc")

    def test_update_task_by_title(self):
        task_list = [Task("Clean the House", "Wipe down counters"),
                    Task("Grocery Store", "Buy bread")]
        #Assuming user wants to update task with title Grocery Store
        task_list = update_task(task_list)
        self.assertEqual(task_list[1].title, "updated title")
        self.assertEqual(task_list[1].desc, "updated desc")
        

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
        taskList = []

        task1 = Task("Clean the House", "Wipe down counters")
        taskList.append(task1)
        task2 = Task("Go to the Grocery Store", "Buy bread")
        taskList.append(task2)
        #Assuming user wants to delete task with index[0]
        taskList = del_task(taskList)
        self.assertEqual(len(taskList), 1)
        self.assertEqual(taskList[0].title, "Go to the Grocery Store")
        self.assertEqual(taskList[0].desc, "Buy bread")

            
        

if __name__ == '__main__':
    unittest.main()


