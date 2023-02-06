import unittest
from controller import add_task

import unittest

class TestAddTask(unittest.TestCase):
    def test_add_task(self):
        taskList = []
        add_task(taskList)

        self.assertEqual(len(taskList), 1)
        self.assertEqual(taskList[0].title, "TestT")
        self.assertEqual(taskList[0].desc, "TestD")
    
        
if __name__ == '__main__':
    unittest.main()


