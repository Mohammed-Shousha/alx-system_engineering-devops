#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""

import csv
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"

    user = requests.get(f"{url}/users/{id}").json()
    user_name = user.get("username")
    todos = requests.get(f"{url}/todos/?userId={id}").json()

    with open(f"{id}.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        [writer.writerow([id,
                          user_name,
                          t.get("completed"),
                          t.get("title")
                          ]) for t in todos]
