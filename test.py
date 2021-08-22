#!/usr/bin/env python3
import json
import requests
import os
import uuid

TOKEN = "" #Put your authorization token here

get_header = {
    "Authorization": f"Bearer {TOKEN}"
}

post_header = {
            "Content-Type": "application/json",
            "X-Request-Id": str(uuid.uuid4()),
            "Authorization": f"Bearer {TOKEN}"
}

def fetch_projects(header):
    raw = requests.request("GET",
                           "https://api.todoist.com/rest/v1/projects",
                           headers= header )
    print(raw.status_code)
    data = raw.json()
    with open('./db.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)


def addTask(header):
    URL = "https://api.todoist.com/rest/v1/tasks"
    blank = {
        "content": "Testing 1",
        "project_id": ""#Put your project iD here
    }
    data = json.dumps(blank)
    raw = requests.post(URL, data = data, headers = header)
    print(raw.status_code)

def getTasks(header):
    URL = "https://api.todoist.com/rest/v1/tasks"
    param = {
        "project_id": ""#Put your project iD here
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
