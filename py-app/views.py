from asyncore import write
from flask import Blueprint, render_template, jsonify, request
import canvas as cv
import json
import requests

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/canvas")
def canvas():
    # writeAssignments(courses)
    # return render_template("canvas.html") 
    data = request.get_json()
    print(data)

    ls = data['array']
    result = sum(ls)
    
    return json.dumps({
        "result": result
    })

@views.route("/node-send")
def nodeSend():
    # courseList = []
    # for course in courses:
    #     courseList += [course.name]
    # data = {
    #     'courses': courseList
    # }
    courses = cv.getCourses()
    assignmentInfo = []
    for course in courses:
        assignments = cv.getAssignments(course)
        for assignment in assignments:
            assignmentdata = {
                "summary": assignment.name,
                # "description": assignment.description,
                "start": {
                    "dateTime": assignment.created_at,
                    "timeZone": "America/Los_Angeles",
                },
                "end": {
                    "dateTime": assignment.due_at,
                    "timeZone": "America/Los_Angeles",
                },
                "client_email": "danielreeder123@gmail.com",
                "reminders": {
                    "useDefault": False,
                    "overrides": [
                        {'method': 'email', 'minutes': 1440},
                    ],
                },
            }
            assignmentJson = json.dumps(assignmentdata)
            assignmentInfo += {assignmentJson}

    res = requests.post('http://127.0.0.1:6000/node-send', json=assignmentInfo)

    returned = res.json()

    print(returned['added'])



    # res = requests.post('http://127.0.0.1:6000/node-send', json=data)

    # returned = res.json()

    # print(returned)
    # result = returned['received']
    # print("Returned from Node.js: ", result)

    return render_template("node-send.html")



