# Import the Canvas class
from re import A
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

# courses = user.get_courses() 

def assignmentsToJson(assignments):
    assignments_Json = []
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
        "id": assignment.id,
        "course-id": assignment.course_id
    })}

def coursesToJson(courses):
    courses_Json = []
    for course in courses:
        courses_Json += courseToJson(course)

    return courses_Json

def courseToJson(course):
    return {{
        "name": course.course_code,
        "id": course.id,
    }}

def writeData(user):
    courses = user.get_courses()
    i = 0
    for course in courses:
        id = "%s"%course.id 
        cFile = "/Users/danielreeder/Desktop/CS407 Project/flask-app/data/courses/" + id + ".json"
        courseFile = open(cFile, 'w')
        cDict = {
            "name": course.course_code,
            "id": course.id
        }
        courseFile.write(json.dumps(cDict, indent=4))
        courseFile.close()
        assignments = course.get_assignments()
        for assignment in assignments:
            id = "%s"%assignment.id
            aFile = "/Users/danielreeder/Desktop/CS407 Project/flask-app/data/assignments/" + id + ".json"
            assignFile = open(aFile, 'w')
            aDict = {
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
                "id": assignment.id,
                "course-id": assignment.course_id
            }
            assignFile.write(json.dumps(aDict, indent=4))
            assignFile.close()
        i += 1
    
def readCourses():
    dir = "/Users/danielreeder/Desktop/CS407 Project/flask-app/data/courses"
    courses = []
    for file in os.listdir(dir):
        rFile = open(os.path.join(dir, file), 'r')
        course = json.load(rFile)
        courses += [course]
    return courses

def readAssignments():
    dir = "/Users/danielreeder/Desktop/CS407 Project/flask-app/data/assignments"
    assignments = []
    for file in os.listdir(dir):
        rFile = open(os.path.join(dir, file), 'r')
        assignment = json.load(rFile)
        assignments += [assignment]
    return assignments
readCourses()
readAssignments()


# writeData(user)
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