#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import json
import requests
import sys


def get_employee_todo_list_progress():
    """_summary_

    Args:
        employee_id (_type_): _description_
    """
    base_url = "https://jsonplaceholder.typicode.com"
    # Fetch all users
    users_response = requests.get(f'{base_url}/users')
    users_data = users_response.json()

    # Create a dictionary to store tasks for each user
    all_tasks = {}

    for user in users_data:
        user_id = user.get('id')
        user_name = user.get('username')

        # Fetch user's TODO list
        todos_return = requests.get(f'{base_url}/todos?userId={user_id}')
        todo_data = todos_return.json()

        # Create JSON data format
        task_list = []
        for task in todo_data:
            task_title = task.get('title')
            task_status = task.get('completed')
            task_dict = {"username": user_name,
                         "task": task_title,
                         "completed": task_status
                         }
            task_list.append(task_dict)

            all_tasks[str(user_id)] = task_list

    # Write to JSON file
    json_filename = 'todo_all_employees.json'
    with open(json_filename, mode='w') as json_file:
        json.dump(all_tasks, json_file)


if __name__ == '__main__':
    get_employee_todo_list_progress()
