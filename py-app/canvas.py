# Import the Canvas class
from canvasapi import Canvas
from datetime import datetime
import pytz

# takes in the due date of an assignment and turns it into a datetime object
def parseDate(date):
    splitDate = date.split("-")
    splitDate[2] = splitDate[2].split("T")
    splitDate.append(splitDate[2][1])
    splitDate[2] = splitDate[2][0]
    splitDate[3] = splitDate[3].replace("Z","")
    splitTime = splitDate[3].split(":")
    dtObject = datetime(int(splitDate[0]), int(splitDate[1]), int(splitDate[2]),
                        int(splitTime[0]), int(splitTime[1]))
    dtObject = pytz.utc.localize(dtObject)
    dtObject = dtObject.astimezone(pytz.timezone("America/Los_Angeles"))
    return dtObject

# Canvas API URL
API_URL = "https://canvas.uoregon.edu"
# Canvas API key
API_KEY = "2391~oad7E1Au5U7jN8WI32Jw4Iq1mS8W3tihD8f9McD5BbCkXLnyxtPnYcvuwdYPXVZR"

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)

me = canvas.get_user(156260)

courseList = me.get_courses()

# counts number of assignments for each course
# prints the due date and name of each assignment
# prints the number of assignments for each course
def printAssignments(courses):
    for course in courses:
        print('\n' + course.name + '\n')
        assignments = course.get_assignments()
        count = 0
        for assignment in assignments:
            count += 1
            print(assignment.name)
            dueDate = parseDate(assignment.due_at)
            print(dueDate.strftime("%B %d, %Y" + " at" + " %I:%M" + '\n'))
        print("Assignment Count: " + str(count) + '\n')
    return course.get_assignments()
    
def writeAssignments(courses):
    with open('assignments.txt', 'w') as f:
        for course in courses:
            f.write(course.name.split(" (")[0] + ',')
