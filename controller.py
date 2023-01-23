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

def del_task(taskList):
    input("What task you want to remove? ")
    name_input = input
    for task in taskList:
        if task.title == name_input:
            index = task.retrieve_idx(taskList)
            taskList.pop(index) #tu w sumie nie wiem 
            task_deleted = taskList.pop(index)
            print(task_deleted)
    
        
    
        

