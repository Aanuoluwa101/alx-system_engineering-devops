#!/usr/bin/python3
"""A module that returns information about an employee's
    todo list progress"""
import json 
import requests
import sys 

if __name__ == '__main__':
    employee_id = sys.argv[1]

    if employee_id and int(employee_id) > 0 and int(employee_id) <= 10:
        url = 'https://jsonplaceholder.typicode.com/users/' + employee_id 
        r = requests.get(url, verify=False)
        name = r.json().get('username')

        url = 'http://jsonplaceholder.typicode.com/users/' \
            + employee_id + '/todos/'
        r = requests.get(url, verify=False)
        todos = r.json()

        filename = employee_id + '.json'
        for task in todos:
            task.pop('userId')
            task.pop('id')
            task['username'] = name
            task['task'] = task.get('title')
            task.pop('title')

        data = {employee_id: todos}
        with open(filename, 'w') as file:
            json.dump(data, file)
