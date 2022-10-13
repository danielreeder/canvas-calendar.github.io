from flask import Blueprint, render_template
from canvas import me, parseDate

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    print("Hello world")
    return render_template("index.html")