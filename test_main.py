import unittest
from controller import add_task, del_task

import unittest

class TestTasks(unittest.TestCase):
    # def test_add_task(self):
    #     taskList = []
    #     add_task(taskList)

    #     self.assertEqual(len(taskList), 1)
    #     self.assertEqual(taskList[0].title, "TestT")
    #     self.assertEqual(taskList[0].desc, "TestD")
    
    def test_del_task(self):
        taskList = [
            {"title": "Cleaning", "desc": "Vacuuming"},
            {"title": "Sports", "desc": "Running"},
            {"title": "Homework", "desc": "Math"}
        ]

        result = del_task(taskList)
        self.assertEqual(len(result), 2)
        self.assertEqual(result, [{"title": "Cleaning", "desc": "Vacuuming"}, 
                                {"title": "Sports", "desc": "Running"}])

if __name__ == '__main__':
    unittest.main()


