from model import Task

def add_task(taskList):
    title = input("\nTask title: ")
    desc = input("\nTask description: ")
    newTask = Task(title, desc)

    taskList.append(newTask)

def list_tasks(taskList):
    for task in taskList:
        index = task.retrieve_idx(taskList)
        print("Task number: ", index)
        print("Task title is: ", task.title)
        print("Task description is: ", task.desc)

#TEST TEST NEW COMMIT TEST

