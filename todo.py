import json
import os

FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f)

def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List ---")
        if tasks:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        else:
            print("No tasks yet.")

        print("\nOptions:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            task = input("Enter new task: ")
            tasks.append(task)
            save_tasks(tasks)

        elif choice == "2":
            try:
                num = int(input("Enter task number to remove: "))
                if 0 < num <= len(tasks):
                    tasks.pop(num-1)
                    save_tasks(tasks)
                else:
                    print("Invalid number")
            except ValueError:
                print("Enter a valid number")

        elif choice == "3":
            print("Exiting. Tasks saved.")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
