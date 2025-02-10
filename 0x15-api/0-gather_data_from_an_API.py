#!/usr/bin/python3
"""
Fetch and display an employee's TODO list progress using a REST API.

Usage: ./script.py <employee_id>
"""

import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]

    # Fetch user data
    user_response = requests.get(f"{base_url}users/{employee_id}")
    user = user_response.json()

    # Fetch todos for the user
    todos_response = requests.get(
        f"{base_url}todos", params={"userId": employee_id}
    )
    todos = todos_response.json()

    # Extract completed tasks
    completed = [todo["title"] for todo in todos if todo["completed"]]

    # Display output
    print(
        f"Employee {user['name']} is done with tasks "
        f"({len(completed)}/{len(todos)}):"
    )
    for task in completed:
        print(f"\t {task}")
