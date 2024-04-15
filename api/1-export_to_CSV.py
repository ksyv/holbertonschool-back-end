#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import csv
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

    # Write to CSV file
    csv_filename = f'{employee_id}.csv'
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for task in todo_data:
            task_completed_status = 'True' if task.get('completed')\
                                    else 'False'
            formatted_row = [employee_id,
                             employee_name,
                             task_completed_status,
                             task.get('title')]
            csv_writer.writerow(formatted_row)

    print(f'Data exported to {csv_filename}')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    employee_id = int(sys.argv[1])
    get_employee_todo_list_progress(employee_id)
