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

    def retrieve_idx(self, taskList):
        index = taskList.index(self)

        return index

    # #Read
    # def print_title(self):
    #     print('Title: ' + self.title)
    # def print_desc(self):
    #     print('Description ' +self.desc)

    #Delete
    #def delete_task(self, list):

