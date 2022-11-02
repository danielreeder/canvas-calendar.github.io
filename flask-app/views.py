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
    return render_template("canvas.html")

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



    # res = requests.post('http://127.0.0.1:6000/node-send', json=data)

    # returned = res.json()

    # print(returned)
    # result = returned['received']
    # print("Returned from Node.js: ", result)

    return render_template("node-send.html")



