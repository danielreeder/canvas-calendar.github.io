from asyncore import write
from flask import Blueprint, render_template, jsonify, request, redirect, url_for
from canvas import writeData, readCourses, readAssignments, user, readFile
import json
import requests
import random as rand
import os
from os.path import exists

views = Blueprint(__name__, "views")

@views.route("/")
def canvas():
    if not exists(os.getenv('COURSE_PATH') + 'exists.txt') and not exists(os.getenv('ASSIGNMENT_PATH') + 'exists.txt'):
        writeData(user)
    courses = readCourses()
    assignments = readAssignments()

    return render_template("canvas.html.j2", courses=courses, assignments=assignments)

@views.route("/update")
def test():
    writeData(user)
    return "nothing"

@views.route("/remove")
def remove(methods=['POST']):
    id = request.args.get('arg')
    file = id + '.json'
    dir = os.getenv('ASSIGNMENT_PATH')
    assignment = readFile(file, dir)
    res = requests.post('http://127.0.0.1:6000/remove', json=assignment)
    returned = res.json()
    print(returned['received'])
    return 'nothing'

@views.route("/add")
def add(methods=['POST']):
    id = request.args.get('arg')
    file = id + '.json'
    dir = os.getenv('ASSIGNMENT_PATH')
    assignment = readFile(file, dir)
    res = requests.post('http://127.0.0.1:6000/add', json=assignment)
    returned = res.json()
    print(returned['received'])
    return 'nothing'