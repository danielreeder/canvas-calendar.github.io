function parseCourses(courses) {
    let courseArr = []
    courses.forEach(element => {
        courseArr.push(JSON.parse(element))
    });

    return courseArr
}

function parseAssignments(assignments) {
    let assignArr = []
    assignments.forEach(element => {
        assignArr.push(JSON.parse(element))
    })

    return assignArr
}
