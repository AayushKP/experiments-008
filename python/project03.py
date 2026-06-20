#Load existing items
# 1. Create a new item
# 2. List Items
# 3. Mark item as complete
# 4. Save items

import json
file_name = "todo_list.json"


def load_tasks():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except:
        return {"tasks":[]}
    
def save_task(tasks):
    try:
        with open(file_name,"w") as file:
            json.dump(tasks,file)
    except:
        print("Failed to save")

def view_tasks(tasks):
    print()
    task_list = tasks["tasks"]
    if len(task_list) == 0:
        print("No task to display")
    else:
        print("Your To-Do List: ")
        for idx,task in enumerate(task_list):
            status = "[Completed]" if task["complete"] else "[Pending]"
            print(f"{idx+1}. {task['description']} | {status}")

def create_task(tasks):
    description = input("Enter the task: ").strip()
    if description:
        tasks["tasks"].append({"description": description, "complete": False})
        save_task(tasks)
        print("Task added.")
    else:
        print("Description cannot be empty")

def mark_task_complete(tasks):
    view_tasks(tasks)

    try:
        task_number = int(input("Enter task no. to be completed: ").strip())

        if 1 <= task_number <= len(tasks["tasks"]):
            tasks["tasks"][task_number - 1]["complete"] = True
            save_task(tasks)
            print("Marked Complete")
        else:
            print("Invalid Task number!")

    except Exception as e:
        print("Error:", e)
        
    view_tasks(tasks)
    try:
        task_number = input("Enter task no. to be completed").strip()
        if 1<= task_number<=len(tasks["tasks"]):
            tasks["tasks"][task_number-1]["complete"] = True
            save_task(tasks)
            print("Marked Complete")
        else:
            print("Invalid Task number!")
    except Exception as e:
        print(e)


def main():
    tasks = load_tasks()
    print(f"{tasks}")

    while True:
        print("\nTo-Do List Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()
        if choice =="1":
            view_tasks(tasks)
        elif choice== "2":
            create_task(tasks)
        elif choice =="3":
            mark_task_complete(tasks)
        elif choice =="4":
            print("Exiting")
            break
        else:
            print("Invalid Choice. Please try again.")

main()