from asyncore import write
from flask import Blueprint, render_template, jsonify, request
from canvas import writeData, readCourses, readAssignments, user
import json
import requests
import random as rand
from os.path import exists

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/canvas")
def canvas():
    if exists("/Users/danielreeder/Desktop/CS407 Project/flask-app/data/courses.txt") and exists("/Users/danielreeder/Desktop/CS407 Project/flask-app/data/assignments.txt"):
        writeData(user)
    courses = readCourses()
    assignments = readAssignments()


    return render_template("canvas.html", courses=courses, assignments=assignments)

@views.route("/update")
def test():
    writeData(user)
    return "nothing"

@views.route("/remove")
def remove(methods=['POST']):
    id = request.args.get('arg')
    json = {
        "id": id
    }
    res = requests.post('http://127.0.0.1:6000/remove', json=json)
    returned = res.json()
    print(returned['received'])
    # print(returned['respond'])
    return 'balls'

@views.route("/node-send")
def nodeSend():
    # courses = canvas.getCourses()
    # assignmentInfo = []
    # for course in courses:
    #     assignments = canvas.getAssignments(course)
    #     for assignment in assignments:
    #         assignmentdata = {
    #             "summary": assignment.name,
    #             "start": {
    #                 "dateTime": assignment.due_at,
    #                 "timeZone": "America/Los_Angeles",
    #             },
    #             "end": {
    #                 "dateTime": assignment.due_at,
    #                 "timeZone": "America/Los_Angeles",
    #             },
    #             "colorId": rand.randint(1,11),
    #         }
    #         assignmentJson = json.dumps(assignmentdata)
    #         assignmentInfo += {assignmentJson}
    #         break

    res = requests.post('http://127.0.0.1:6000/node-send', json=readCourses())

    returned = res.json()

    print(returned['added'])
    return render_template("node-send.html")



