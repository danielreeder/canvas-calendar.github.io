// const request = require('request-promise')
const express = require('express')
const bodyParser = require('body-parser')
require('dotenv').config()
const google = require('./google-int')

var app = express()

app.use(bodyParser.json())
app.use(bodyParser.urlencoded({
    extended: false
}))

app.post("/node-send", (req, res) => {
    var count = 0
    req.body.forEach(element => {
      google.addAssignment(element)
      console.log('Assignment added')
      count += 1
    });
    console.log(google.listEvents())

    res.json({
      received: 'true',
      added: count
    })
})

app.post("/remove", (req, res) => {
    console.log(req.body)
    date = new Date()
    test = {
      calendarId: 'primary',
      summary: 'test',
      id: req.body.id,
      start: {
        dateTime: date,
        timeZone: 'America/Los_Angeles',
      },
      end: {
        dateTime: date,
        timeZone: 'America/Los_Angeles',
      },
    }
    // response = google.addAssignment(test)
    response = google.removeAssignment(req.body.id)

    res.json({
      received: 'true',
      respond: response
    })
})

app.listen(6000)