#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import json
import requests
import sys


def get_employee_todo_list_progress(employee_id):
    """_summary_

    Args:
        employee_id (_type_): _description_
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(base_url, employee_id)
    todo_url = "{}/todos?userId={}".format(base_url, employee_id)

    # userdata for get employee name with id:
    user_return = requests.get(user_url)
    user_data = user_return.json()
    user_name = user_data.get('username')

    # Task data for get number of done tasks and total number of tasks
    todo_return = requests.get(todo_url)
    todo_data = todo_return.json()

    # Create JSON data format
    task_list = []
    for task in todo_data:
        task_title = task.get('title')
        task_status = task.get('completed')
        task_dict = {"task": task_title,
                     "completed": task_status,
                     "username": user_name}
        task_list.append(task_dict)

    json_data = {str(employee_id): task_list}

    # Write to JSON file
    json_filename = f'{employee_id}.json'
    with open(json_filename, mode='w') as json_file:
        json.dump(json_data, json_file)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    employee_id = int(sys.argv[1])
    get_employee_todo_list_progress(employee_id)
