from asyncore import write
from flask import Blueprint, render_template, jsonify, request
import canvas as cv
import json
import requests
import random as rand

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/canvas")
def canvas():
    # needs to take all classes and assignments as json and pass to html
    # to be dealt with in javascript
    data = {'username': 'divinemamma', 'password': 'yahoo1'}
    return render_template("canvas.html", data=data)

@views.route("/node-send")
def nodeSend():
    courses = cv.getCourses()
    assignmentInfo = []
    for course in courses:
        assignments = cv.getAssignments(course)
        for assignment in assignments:
            assignmentdata = {
                "summary": assignment.name,
                "start": {
                    "dateTime": assignment.due_at,
                    "timeZone": "America/Los_Angeles",
                },
                "end": {
                    "dateTime": assignment.due_at,
                    "timeZone": "America/Los_Angeles",
                },
                "colorId": rand.randint(1,11),
            }
            assignmentJson = json.dumps(assignmentdata)
            assignmentInfo += {assignmentJson}
            break

    res = requests.post('http://127.0.0.1:6000/node-send', json=assignmentInfo)

    returned = res.json()

    print(returned['added'])
    return render_template("node-send.html")



