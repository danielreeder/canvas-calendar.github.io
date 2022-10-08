const canvasAPI = require('node-canvas-api')

// canvasAPI.getSelf()
//     .then(self => console.log(self))

// canvasAPI.getCoursesByUser(156260)
//     .then(courses => console.log(courses))

canvasAPI.getAssignments(210956)
    .then(assignments => assignments.forEach(assignment => console.log(assignment.due_at)))