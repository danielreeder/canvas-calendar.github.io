function parseCourses(courses){
    let courseArr = []
    courses.forEach(element => {
        courseArr.push(JSON.parse(element))
    });

    return courseArr
}
