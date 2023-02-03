from model import Task

def add_task(taskList):
    title = input("\nTask title: ")
    desc = input("\nTask description: ")
    newTask = Task(title, desc)

    taskList.append(newTask)

def update_task(taskList):
    name_or_index = input("What task you want to update? Enter the title or index: ")
    try:
        index = int(name_or_index)
        if index < 0 or index >= len(taskList):
            raise ValueError("Index out of range")
        task = taskList[index]
    except ValueError:
        for t in taskList:
            if t.title == name_or_index:
                task = t
                break
        else:
            print("Task not found")
            return

    new_title = input("Enter the new title: ")
    new_desc = input("Enter the new description: ")
    task.title = new_title
    task.desc = new_desc
    print(f"Task {name_or_index} has been updated to {new_title} with description {new_desc}")

    

def list_tasks(taskList):
    if len(taskList) == 0:
        print("The list is empty!")
        return
    for task in taskList:
        index = taskList.index(task)
        print("Task number: ", index)
        print("Task title is: ", task.title)
        print("Task description is: ", task.desc)


def del_task(taskList):
    name_or_index = input("What task you want to remove? Enter the title or task number: ")
    try:
        index = int(name_or_index)
        if index < 0 or index >= len(taskList):
            raise ValueError("Index out of range")
        task_deleted = taskList.pop(index)
        print(task_deleted.title, "has been deleted")
    except ValueError:
        for task in taskList:
            if task.title == name_or_index:
                taskList.remove(task)
                print(task.title, "has been deleted")
                break
        else:
            print("Task not found")
    
        

