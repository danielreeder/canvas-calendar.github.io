function reloadPage() {
    window.location.reload()
}

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
    assignByCourse.forEach(array => {
        array = array.sort((date1, date2) => {
            if (date1.start.dateTime && date2.start.dateTime){
                date3 = new Date(date1.start.dateTime)
                date4 = new Date(date2.start.dateTime)
                return date4.getTime() - date3.getTime()
            }
            else {
                return 1
            }
        })

    })
    console.log(assignByCourse)

    return assignByCourse
}

function createClassScroll(course, assigns) {
    const months = ['January', 'February', 'March', 'April', 'May', 'June',
                    'July', 'August', 'September', 'October', 'November', 'December']
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
        dueDate = new Date(assign.start.dateTime)
        today = new Date()
        time = today.getTime()
        dateStr = 'Due: ' + months[dueDate.getMonth()] + ' ' + dueDate.getDate() + ' at ' + 
                         dueDate.getHours()%12 + ':' + (dueDate.getMinutes() < 10 ? '0'+dueDate.getMinutes() : dueDate.getMinutes())
                        + (dueDate.getHours() >= 12 ? ' P.M.' : ' A.M.')
        let assignContainer = document.createElement("div")
        assignContainer.classList.add('assignment-container', 'shadow-card')
        let assignHeader = document.createElement("div")
        assignHeader.classList.add('assignment-header')
        let assignHeaderText = document.createElement("h4")
        assignHeaderText.classList.add('assignment-header-text')
        assignHeaderText.textContent = assign.summary
        let dateText = document.createElement("h5")
        dateText.classList.add('date-text')
        dateText.textContent = dateStr
        assignHeader.id = assign.id
        assignHeader.append(assignHeaderText)
        assignHeader.append(dateText)
        assignContainer.append(assignHeader)
        let addBtn = document.createElement('a')
        addBtn.classList.add('btn', 'add-btn')
        addBtn.textContent = 'Add to Calendar'
        let btnContainer = document.createElement('div')
        btnContainer.classList.add('btn-container')
        let removeBtn = document.createElement('a')
        removeBtn.classList.add('btn', 'remove-btn', 'two-btn')
        addBtn.classList.add('two-btn')
        removeBtn.textContent = "Remove from Calendar"
        btnContainer.append(addBtn)
        btnContainer.append(removeBtn)
        if (dueDate.getTime() < time) {
            assignContainer.classList.add('old-assign')
        }
        
        assignContainer.append(btnContainer)
        assignmentsContainer.append(assignContainer)
    })

    scroll.append(assignmentsContainer)
    document.body.append(scroll)
}