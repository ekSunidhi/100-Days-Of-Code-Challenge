import os

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks, new_task):
    tasks.append(new_task)
    print("Task added successfully.")

def remove_task(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print(f"Removed task: {removed_task}")
    else:
        print("Invalid task index.")

def save_to_file(tasks, filename="tasks.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def main():
    filename = "tasks.txt"
    tasks = []

    if os.path.exists(filename):
        with open(filename, "r") as file:
            tasks = file.read().splitlines()

    while True:
        print("\nTo-Do List Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Save and Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            new_task = input("Enter the task: ")
            add_task(tasks, new_task)
        elif choice == "3":
            task_index = int(input("Enter the task number to remove: "))
            remove_task(tasks, task_index)
        elif choice == "4":
            save_to_file(tasks, filename)
            print("To-Do list saved. Exiting.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
