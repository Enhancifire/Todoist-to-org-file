#!/usr/bin/env python3

import json
import requests
import os
import uuid

TOKEN = "" #Insert your token here
get_header = {
    "Authorization": f"Bearer {TOKEN}"
}
post_header = {
            "Content-Type": "application/json",
            "X-Request-Id": str(uuid.uuid4()),
            "Authorization": f"Bearer {TOKEN}"
}
def getTasks(header):
    URL = "https://api.todoist.com/rest/v1/tasks"
    param = {
        "project_id": "" #your project id (numbers) here
    }
    raw = requests.get(URL, params = param, headers = header)
    return raw.json()

tasks = getTasks(get_header)
no_of_tasks = len(tasks)

taskList = []
for i in range(0, no_of_tasks):
    tempList = [tasks[i]['content'], tasks[i]['due']['date']]
    taskList.append(tempList)

def Sort(sub_li):
    sub_li.sort(key = lambda x: x[1])
    return sub_li

taskList = Sort(taskList)
list_len = len(taskList)
with open("schedule.org", "w") as f:
    for i in range(0, list_len):
        f.write(
            f'''* {taskList[i][0]}
SCHEDULED: <{taskList[i][1]}>'''+"\n"
            )
