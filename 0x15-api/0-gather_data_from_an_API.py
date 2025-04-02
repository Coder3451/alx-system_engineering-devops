#!/usr/bin/python3
import requests
import sys

"""
This script fetches and prints the task completion status for a employee ID.
"""

def main():
    """Main function to fetch and display employee task data."""
    employee_id = int(sys.argv[1])

    response = requests.get(
            f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )

    if response.status_code != 200:
        print("Error fetching data")
        return

    todos = response.json()

    employee_name = todos[0]['userId'] if todos else "Unknown"

    completed_tasks = [
            task['title'] for task in todos if task['completed']
    ]
    total_tasks = len(todos)

    print(
            f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):"
    )
    for task in completed_tasks:
        print(f"\t {task}")


if __name__ == "__main__":
    main()
