#!/usr/bin/python3
"""A module that returns information about an employee's
    todo list progress"""
import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]

    if employee_id and int(employee_id) > 0 and int(employee_id) <= 10:
        url = 'https://jsonplaceholder.typicode.com/users/' + employee_id
        r = requests.get(url, verify=False)
        name = r.json().get('name')

        url = 'http://jsonplaceholder.typicode.com/users/' \
            + employee_id + '/todos/'
        r = requests.get(url, verify=False)
        todos = r.json()

        total_tasks = 0
        done = []
        done_count = 0

        for todo in todos:
            if todo.get('completed'):
                done_count += 1
                done.append(todo.get('title'))
            total_tasks += 1

        print("Employee {} is done with tasks({}/{}):"
              .format(name, done_count, total_tasks))
        if done_count > 0:
            for task in done:
                print("\t {}".format(task))
