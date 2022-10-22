from asyncore import write
from flask import Blueprint, render_template, jsonify, request
from canvas import courses, writeAssignments
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
    courseList = []
    for course in courses:
        courseList += [course.name]
    data = {
        'courses': courseList
    }

    res = requests.post('http://127.0.0.1:3000/node-send', json=data)

    returned = res.json()

    print(returned)
    result = returned['received']
    print("Returned from Node.js: ", result)

    return render_template("canvas.html")



