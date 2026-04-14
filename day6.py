tasks = [
    {"task": "buy groceries", "done": False},
    {"task": "Study pythob", "done": False},
    {"task": "Talk to Piyu", "done": False},
    {"task": "Talk to mom", "done": False}
]

def show_menu():
    print("--- To-Do-List ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task complete")
    print("4. Delete tasks")
    print("5. Quit")
    return int(input("Enter your choice: "))



def add_task(tasks):
    add = input("Enter your task: ")
    tasks.append({"task": add, "done": False})

def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks yet!")
    for index, task in enumerate(tasks):
        if task["done"]:
            status = "[x]"
        else:
            status = "[ ]"
        print(f"{index + 1}. {task['task']} - {status}")

def complete_task(tasks):
    view_tasks(tasks)
    choice = int(input("Enter the task number to mark complete: "))
    tasks[choice - 1]["done"] = True

def delete_task(tasks):
    view_tasks(tasks)
    option = int(input("Enter the choice you want to delete: "))
    tasks.pop(option - 1)


def run_app(tasks):
    while True:
        choice = show_menu()
        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            view_tasks(tasks)
        elif choice == 3:
            complete_task(tasks)
        elif choice == 4:
            delete_task(tasks)
        elif choice == 5:
            print("Goodbye!")
            break

run_app(tasks)