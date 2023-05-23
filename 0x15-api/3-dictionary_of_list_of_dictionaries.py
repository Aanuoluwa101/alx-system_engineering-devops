#!/usr/bin/python3
"""A module that returns information about an employee's
    todo list progress"""
import json
import requests
import sys

if __name__ == '__main__':

    def getTodos(employee_id):
        """Gets the todo list of an employee"""
        url = 'https://jsonplaceholder.typicode.com/users/' + employee_id
        r = requests.get(url, verify=False)
        name = r.json().get('username')

        url = 'http://jsonplaceholder.typicode.com/users/' \
            + employee_id + '/todos/'
        r = requests.get(url, verify=False)
        todos = r.json()

        for task in todos:
            task.pop('userId')
            task.pop('id')
            task['username'] = name
            task['task'] = task.get('title')
            task.pop('title')
        return todos

    data = {}
    for i in range(1, 11):
        i = str(i)
        data[i] = getTodos(i)

    filename = "todo_all_employees.json"
    with open(filename, 'w') as file:
            json.dump(data, file)
