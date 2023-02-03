from controller import add_task, list_tasks, del_task, update_task




def main():        
        task_list = []

        while True:
                print('''
                1: 'Create new task',
                2: 'Update specific task',
                3: 'Show all tasks',
                4: 'Delete specific task',
                5: 'Exit',
                ''')
                print()
                option = int(input('Enter your choice: ')) 
                if option == 1:
                        add_task(task_list)
                if option == 2:
                        update_task(task_list)
                if option == 3:
                        list_tasks(task_list)
                if option == 4:
                        del_task(task_list)
                        
                elif option == 5:
                        print("Thanks for using my task list!")
                        exit()
                        

if __name__ == "__main__":
         main()












