function parseCourses(courses) {
    let courseArr = []
    courses.forEach(element => {
        courseArr.push(element)
    });
    console.log(typeof courses)
    console.log(courses)
    return courseArr
}


// next thing to do, figure out how to sort assignments by course
function parseAssignments(assignments) {
    let assignArr = []
    assignments.forEach(element => {
        assignArr.push(element)
    })


    console.log(assignments)
    return assignArr
}
