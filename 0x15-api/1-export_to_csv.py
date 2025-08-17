#!/usr/bin/python3
"""
Exports data from a REST API to CSV format.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    # Get user ID
    user_id = sys.argv[1]

    # API endpoint
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")

    # Fetch todo
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # Write to CSV
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]
