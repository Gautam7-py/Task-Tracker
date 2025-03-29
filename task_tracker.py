import json
import os

task_list = "data.json"

def add_tasks(des):
    if des:
        new_task ={
            "id" : len(task_list) + 1,
            "description": des,
            "status": "todo"
        }
        task_list.append(new_task)

        with open("task_list", "w") as f:
            json.dump(task_list, f , indent = 2)

        print(f"Task added successfully: {new_task['id']}")
    else:
        print("Task description cannot be empty.")

def update_task(id, description):
    for task in task_list:
        if task['id'] == id:
            task['descripton'] = description

            with open("task_list", "w") as f:
                json.dump(task_list, f, indent=2)

            print(f"Task {id} updated successfully.")
            break
    else:
        print(f"Task with ID {id} not found.")

def delete_task(id):
    for task in task_list:
        if task['id'] == id:
            task_list.remove(task)

            with open("task_list", "w") as f:
                json.dump(task_list, f, indent=2)

            print(f"Task {id} deleted successfully.")
            break
    else:
        print(f"Task with ID {id} not found.")

def list_tasks_all():
    try:
        with open("task_list") as f:
            task_list = json.load(f)
        return task_list
    except FileNotFoundError:
        return []

def list_tasks_done():
    tasks_done = []
    try:
        with open ("task_list") as f:
            task_list = json.load(f)
        for task in task_list:
            if task["status"] == "done":
                tasks_done.append(task)
        return task
    except FileNotFoundError:
        return []

def list_tasks_notdone():
    tasks_notdone = []
    try:
        with open ("task_list") as f:
            task_list = json.load(f)
        for task in task_list:
            if task["status"] == "not-done":
                tasks_notdone.append(task)
        return task
    except FileNotFoundError:
        return []

def list_tasks_inprogress():
    tasks_inprogress = []
    try:
        with open ("task_list") as f:
            task_list = json.load(f)
        for task in task_list:
            if task["status"] == "in-prpgress":
                tasks_inprogress.append(task)
        return task
    except FileNotFoundError:
        return []




def main():
    print("Welcome to Task Tracker")
    commands = {
        "list": list_tasks_all,
        "list-done": list_tasks_done,
        "list-notdone": list_tasks_notdone,
        "list-inprogress": list_tasks_inprogress,
    }

    while True:
        command = input("task-cli>").strip().split(" ", 1)

        if not command:
            continue

        elif command in commands:
            task_list = commands[command]()
            if task_list:
                for task in task_list:
                    print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")
            else:
                print("No tasks found.")
                

        elif command[0] == "add":
            if len(command) > 1:
                add_tasks(command[1])
            else:
                print("Usage: add <task_description>")


        elif command[0] == "update":
            if len(command) > 1:
                command_parts = command[1].split(" ", 1)
                if len(command_parts) > 1:
                    try:
                        task_id = int(command_parts[0])
                        des = command_parts[1]
                        update_task(task_id, des)
                    except ValueError:
                        print("Invalid task ID. Please provide a number.")
                else:
                    print("Usage: update <task_id> <new_description>")
            else:
                print("Usage: update <task_id> <new_description>")


        elif command[0] == "delete":
            if len(command) > 1:
                try:
                    task_id = int(command[1])
                    delete_task(task_id)
                except ValueError:
                    print("Invalid task ID. Please provide a number.")
            else:
                print("Usage: delete <task_id>")

        elif command[0] == "exit":
            print("Exiting Task Tracker.")
            break
        else:
            print("Unknown command. Available commands: list, add, update, delete, exit")


if __name__ == "__main__":
    main()





        
                


        
    
        