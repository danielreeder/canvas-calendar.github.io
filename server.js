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

app.listen(6000)