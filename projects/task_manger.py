import json
tasks=[]
while True:
    print("=== Task Manager ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Mark Task as Not Done ")
    print("5. Delete a Task ")
    print("6. Save Tasks")
    print("7. Load Tasks")
    print("8. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Adding a task...")
        task = { "title": "", "done": False }
        title = input("Enter the title of the task: ")
        task["title"] = title
        tasks.append(task)
        print("Task added!")
    elif choice == 2:
        print("Viewing tasks...")
        for index, task in enumerate(tasks):
            box = "✅" if task["done"] else "⬜"
            print(f"{ box } {index + 1}. {task['title']}")
        if not tasks:
            print("No tasks found. Add something first!")
    elif choice == 3:
        print("Marking task as done...")
        task_num= int(input("Enter the task number to mark as done: "))
        try:
            index= task_num - 1
            tasks[index]["done"] = True
            print(f"Task {task_num} marked as done!")
        except IndexError:
            print("Invalid task number. Please try again.")
    elif choice == 4:
        for index, task in enumerate(tasks):
             box = "✅" if task["done"] else "⬜"
             print(f"{index + 1}. {box} {task['title']}")
        try:
            task_num = int(input("Enter task number to mark as NOT done: ")) - 1
            tasks[task_num]["done"] = False
            print("Task marked as NOT done ❌")
        except:
             print("Invalid number. Please try again.")
    elif choice == 5:
        print("Deleting a task...")
        task_num = int(input("Enter task number to delete: ")) - 1
        try:
            tasks.pop(task_num)
            print("Task deleted! 🗑️")
        except IndexError:
            print("Invalid task number. Please try again.")

    elif choice == 6:
        print("Saving tasks...")
        with open("tasks.json", "w") as file:
            json.dump(tasks, file)
        print("Tasks saved to tasks.json ✅")
    elif choice == 7:
        print("Loading tasks...")
        try:
          with open("tasks.json", "r") as file:
           tasks = json.load(file)
          print("Tasks loaded from file ✅")
        except FileNotFoundError:
             print("No saved tasks found.")

    elif choice == 8:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")