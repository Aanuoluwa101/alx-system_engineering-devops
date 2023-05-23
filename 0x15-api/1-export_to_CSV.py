#!/usr/bin/python3
"""A module that returns information about an employee's
    todo list progress"""
import csv
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

        fieldnames = ['userId', 'name', 'completed', 'title']
        filename = employee_id + '.csv'

        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            if todos:
                for task in todos:
                    task['name'] = name
                    writer.writerow({key: value for key, value 
                                     in task.items() if key != 'id'})
