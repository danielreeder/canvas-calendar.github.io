// if (process.env.NODE_ENV !== 'production'){
//     require('dotenv').config
// }

// const CANVAS_API_KEY = process.env.CANVAS_API_KEY
// const { default: axios } = require('axios')
// const express = require('express')
// const app = express()

// app.use(express.json())
// app.use(express.static('public'))

// app.post('/user', (req, res) => {
//     url = 'https://canvas.instructure.com/api/v1/courses?access_token=${CANVAS_API_KEY}/'
//     axios({
//         url: url,
//         responseType: 'json'
//     }).then(data => data.data)
// })

// app.listen(8000, () => {
//     console.log('Server has started')
// })

var request = require('request-promise')
var express = require('express')
var bodyParser = require('body-parser')

var app = express()

app.use(bodyParser.json())
app.use(bodyParser.urlencoded({
    extended: false
}))

app.post("/canvas", (req, res) => {
    var courses = req.body.courses
    console.log(courses)

    res.json({
        received: "true"
    })
})

app.listen(3000)