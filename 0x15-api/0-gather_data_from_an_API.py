#!/usr/bin/python3
import sys
import requests

if len(sys.argv) != 2:
    print("Usage: {} <employee_id>".format(sys.argv[0]))
    sys.exit(1)

employee_id = sys.argv[1]

url = "".format(employee_id)
response = requests.get(url)

if response.status_code != 200:
    print("Failed to retrieve data")
    sys.exit(1)

data = response.json()

total_tasks = len(data)
completed_tasks = [task for task in data if task.get("completed") is True]
num_completed = len(completed_tasks)

employee_name = "Employee_Name_Not_Found"

print("Employee {} is done with tasks({}/{})".format(employee_name, num_completed, total_tasks))

for task in completed_tasks:
    print("\t {}".format(task.get("title"))
