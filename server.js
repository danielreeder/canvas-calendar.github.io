// const request = require('request-promise')
const express = require('express')
const bodyParser = require('body-parser')
require('dotenv').config()
const google = require('./google-int')
const { response } = require('express')
const fs = require('fs')

var app = express()

app.use(bodyParser.json())
app.use(bodyParser.urlencoded({
    extended: false
}))

// app.post("/node-send", (req, res) => {
//     var count = 0
//     req.body.forEach(element => {
//       google.addAssignment(element)
//       console.log('Assignment added')
//       count += 1
//     });
//     console.log(google.listEvents())

//     res.json({
//       received: 'true',
//       added: count
//     })
// })

app.post("/remove", (req, res) => {
  let response = google.removeAssignment(req.body)

  res.json({
    received: 'true',
    respond: response === 'Calendar event does not exists' ? response : null
  })
})

app.post("/add", (req, res) => {
  let response = google.addAssignment(req.body)
  res.json({
    received: 'true',
    respond: response === 'Calendar event already exists' ? response : null
  })
})

app.listen(6000)