function parseCourses(courses) {
    let courseArr = []
    let courseIds = []
    courses.forEach(course => {
        courseIds.push(course.id)
    })
    courseIds.sort()
    courses.forEach(course => {
        courseIndex = courseIds.indexOf(course.id)
        courseArr[courseIndex] = course
    });
    console.log(courseArr)
    return courseArr
}


function parseAssignments(assignments, courses) {
    let assignArr = []
    courseIds = new Array(courses.length)
    courses.forEach(course => {
        courseIds.push(course.id)
    })
    courseIds.sort()
    assignByCourse = new Array(courses.length)
    assignments.forEach(assign => {
        assignIndex = courseIds.indexOf(assign.courseId)
        if (!assignByCourse[assignIndex]){
            assignByCourse[assignIndex] = new Array
        }
        assignByCourse[assignIndex].push(assign)
    })
    console.log(assignByCourse)

    return assignByCourse
}

function createClassScroll(course, assigns) {
    let courseName = course.name
    const date = new Date()
    let scroll = document.createElement("div")
    scroll.classList.add("class-scroll", "shadow-card")
    let header = document.createElement("div")
    header.classList.add('class-header-container', 'shadow-card')
    let headerText = document.createElement("h2")
    headerText.classList.add('class-header')
    headerText.textContent = courseName
    header.append(headerText)
    scroll.append(header)
    let assignmentsContainer = document.createElement("div")
    assignmentsContainer.classList.add('assignments-container')

    assigns.forEach(assign => {
        let assignContainer = document.createElement("div")
        assignContainer.classList.add('assignment-container', 'shadow-card')
        let assignHeader = document.createElement("div")
        assignHeader.classList.add('assignment-header', 'shadow-card')
        let assignHeaderText = document.createElement("h4")
        assignHeaderText.classList.add('assignment-header-text')
        assignHeaderText.textContent = assign.summary
        assignHeader.append(assignHeaderText)
        assignContainer.append(assignHeader)
        assignmentsContainer.append(assignContainer)
    })

    scroll.append(assignmentsContainer)
    document.body.append(scroll)
}