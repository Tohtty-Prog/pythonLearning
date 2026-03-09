import json
import os


def check_file():
    if not os.path.exists("todo.json"):
        with open("todo.json", 'w') as f:
            json.dump({"tasks": []}, f, indent=4)

def add_task(task):
    with open("todo.json", 'r') as f:
        data = json.load(f)

        new_task = {
            "task": task
        }

        data["tasks"].append(new_task)
    
    with open("todo.json", 'w') as f:
        json.dump(data, f, indent=4)

def remove_task(task_number):
    with open("todo.json", 'r') as f:
        data = json.load(f)
    if 0 < task_number <= len(data["tasks"]):
        del data["tasks"][task_number - 1]

        with open("todo.json", 'w') as f:
            json.dump(data,f,indent=4)
    else:
        print("invalid task number")

def show_tasks():
    with open("todo.json", 'r') as f:
        data = json.load(f)
    if not data["tasks"]:
        print("No tasks")
        return
    
    for i,task in enumerate(data["tasks"], start=1):
        print(f"{i}. task: {task}")

def main():
    check_file()

    while True:
        print("\n1. Add task")
        print("2. Remove task")
        print("3. Show tasks")
        print("4. Exit")

        choice = input("Choice: ")

        if choice == '1':
            task = input("Task to add: ")
            add_task(task)
        elif choice == '2':
            task_number = int(input("Which task to remove: "))
            remove_task(task_number)
        elif choice == '3':
            show_tasks()
        elif choice == '4':
            print("Bye")
            break
        else:
            print("Unknown choice")       


if __name__ == "__main__":
    main()