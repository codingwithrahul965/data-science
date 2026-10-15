tasks =[]

def add_task():
    task = input("Enter task:")
    tasks.append(task)
    print("task added")
def show_tasks():
    if len(tasks) == 0:
        print("no tasks found")
    else:
        for i in range(len(tasks)):
            print(i , "-", tasks[i])
def delete_task():
    show_tasks()
    index = int(input("Enter task index to delete:")) 
    if 0<= index < len(tasks):
        tasks.pop(index)
        print("task deleted")  
    else:
        print("invalid index")     

while True:
    print("\n1. Add Task")
    print("2. Show Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        delete_task()

    elif choice == "4":
        break

    else:
        print("Invalid choice")        

