# view_tasks.py

def view_tasks():
    """Displays all tasks in the to-do list."""
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if tasks:
                print("To-Do List:")
                for idx, task in enumerate(tasks, 1):
                    print(f"{idx}. {task.strip()}")
            else:
                print("The to-do list is empty!")
    except FileNotFoundError:
        print("No tasks found! Start by adding a task.")


if __name__ == "__main__":
    view_tasks()
