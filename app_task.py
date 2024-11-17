# add_task.py

def add_task(task):
    """Adds a new task to the to-do list."""
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print(f"Task '{task}' added successfully!")


if __name__ == "__main__":
    task = input("Enter the task you want to add: ")
    add_task(task)