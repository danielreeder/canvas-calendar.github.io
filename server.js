const request = require('request-promise')
const express = require('express')
const bodyParser = require('body-parser')
require('dotenv').config()
const google = require('./google-auth')

var app = express()

app.use(bodyParser.json())
app.use(bodyParser.urlencoded({
    extended: false
}))

app.post("/node-send", (req, res) => {
    // var courses = req.body.courses
    // console.log(courses)

    // res.json({
    //     received: google.sum()
    // })
    console.log(req.body)
    var count
    req.body.forEach(element => {
      google.addAssignment(element)
      console.log('Assignment added')
      count++
    });

    res.json({
      received: 'true',
      added: count
    })
})

app.listen(6000)