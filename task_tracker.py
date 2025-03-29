import json
import os

task_list = "data.json"

def add_tasks(task):
    if task:
        new_task ={
            "id" : len(task_list) + 1,
            "description": task,
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






        
    
        