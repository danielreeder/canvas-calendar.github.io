# Import the Canvas class
from canvasapi import Canvas
import os
from dotenv import load_dotenv
import random as rand
import json
load_dotenv()

# Canvas API URL
API_URL = os.getenv('CANVAS_URL')
# Canvas API key
API_KEY = os.getenv('CANVAS_API_KEY')

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)

user = canvas.get_user(156260)

courses = user.get_courses() 

def assignmentsToJson(courses):
    assignments_Json = []
    for course in courses:
        assignments = course.get_assignments()
        for assignment in assignments:
            assignments_Json += assignmentToJson(assignment)
            
    return assignments_Json


def assignmentToJson(assignment):
    return {json.dumps({
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
        "id": assignment.id
    })}

def coursesToJson(courses):
    courses_Json = []
    for course in courses:
        courses_Json += courseToJson(course)

    return courses_Json

def courseToJson(course):
    return {json.dumps({
        "name": course.course_code,
        "id": course.id,
    })}


# def main():
#     # Canvas API URL
#     API_URL = os.getenv('CANVAS_URL')
#     # Canvas API key
#     API_KEY = os.getenv('CANVAS_API_KEY')

#     # Initialize a new Canvas object
#     canvas = Canvas(API_URL, API_KEY)

#     me = canvas.get_user(156260)

#     courses = me.get_courses() 
#     print(assignmentsToJson(courses))
#     print(coursesToJson(courses))
# main()