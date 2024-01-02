#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""

import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"

    users = requests.get(f"{url}/users").json()

    with open("todo_all_employees.json", "w") as json_file:
        json.dump({
            user.get("id"): [{
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username")
            } for todo in requests.get(
                f"https://jsonplaceholder.typicode.com/todos/"
                f"?userId={user.get('id')}")
                .json()]
            for user in users}, json_file)
