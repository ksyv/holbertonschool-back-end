#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""

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
    employee_name = user_data.get('name')

    # Task data for get number of done tasks and total number of tasks
    todo_return = requests.get(todo_url)
    todo_data = todo_return.json()
    total_number_of_tasks = len(todo_data)
    number_of_done_tasks = sum(task.get("completed", False)
                               for task in todo_data)

    # print first line
    print("Employee {} is done with tasks ({}/{}):".format(
        employee_name, number_of_done_tasks, total_number_of_tasks), end='\n')

    # print second and N next line:
    for task in todo_data:
        if task.get("completed", False):
            print("\t {}".format(task.get("title")))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    employee_id = int(sys.argv[1])
    get_employee_todo_list_progress(employee_id)
