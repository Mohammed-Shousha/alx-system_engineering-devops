#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""

import json
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"

    user = requests.get(f"{url}/users/{id}").json()
    user_name = user.get("username")
    todos = requests.get(f"{url}/todos/?userId={id}").json()

    with open(f"{id}.json", "w") as json_file:
        json.dump({id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": user_name
            } for t in todos]}, json_file)
