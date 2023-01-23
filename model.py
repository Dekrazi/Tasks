class Task:
    #Create
    def __init__(self, title, desc):
        self.title = title
        self.desc = desc

    #Update
    def title_change(self, new_title):
        self.title = new_title

    def desc_change(self, new_desc):
        self.desc = new_desc
    #Read
    def retrieve_idx(self, taskList):
        index = taskList.index(self)
        return index
    #Delete
    def del_task(self, taskList):
        del_task = input(taskList.remove())    

   
