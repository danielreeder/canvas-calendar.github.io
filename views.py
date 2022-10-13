from asyncore import write
from flask import Blueprint, render_template, jsonify
from canvas import courseList as courses, writeAssignments

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("canvas")
def canvas():
    writeAssignments(courses)
    return render_template("index.html") 
