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
    dir = os.getenv('COURSE_PATH')
    for file in os.listdir(dir):
        os.remove(os.path.join(dir,file))
    dir = os.getenv('ASSIGNMENT_PATH')
    for file in os.listdir(dir):
        os.remove(os.path.join(dir,file))
    courses = user.get_courses()
    i = 0
    for course in courses:
        id = "%s"%course.id 
        cFile = os.getenv('COURSE_PATH') + id + ".json"
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
            aFile = os.getenv('ASSIGNMENT_PATH')+ id + ".json"
            print(aFile)
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
                "courseId": assignment.course_id,
                "status": "confirmed"
            }
            assignFile.write(json.dumps(aDict, indent=4))
            assignFile.close()
        i += 1
    existPath = os.getenv('COURSE_PATH') + 'exists.txt'
    existFile = open(existPath, 'w')
    existFile.write('exists')
    existPath = os.getenv('COURSE_PATH') + 'exists.txt'
    existFile = open(existPath, 'w')
    existFile.write('exists')
    
def readCourses():
    dir = os.getenv('COURSE_PATH')
    courses = []
    for file in os.listdir(dir):
        if 'exists' not in file:
            courses += [readFile(file, dir)]
    return courses

def readAssignments():
    dir = os.getenv('ASSIGNMENT_PATH')
    assignments = []
    for file in os.listdir(dir):
        if 'exists' not in file:
            assignments += [readFile(file, dir)]
    return assignments

def readFile(file, dir):
    rFile = open(os.path.join(dir, file), 'r')
    contents = json.load(rFile)
    return contents

    
# readCourses()
# readAssignments()


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