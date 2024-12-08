def remove_task(task_number):
    """Removes a task from the to-do list by its number."""
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        
        if 0 < task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print(f"Task '{removed_task.strip()}' removed successfully!")
        else:
            print("Invalid task number!")
    except FileNotFoundError:
        print("No tasks found! Start by adding a task.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    try:
        task_number = int(input("Enter the task number to remove: "))
        remove_task(task_number)
    except ValueError:
        print("Please enter a valid number.") 