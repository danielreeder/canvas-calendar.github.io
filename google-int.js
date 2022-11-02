const { google } = require('googleapis')
const { OAuth2 } = google.auth
require('dotenv').config()
const oAuth2Client = new OAuth2(process.env.CLIENT_ID, process.env.CLIENT_SECRET)

oAuth2Client.setCredentials({
    refresh_token: process.env.REFRESH_TOKEN
})

const calendar = google.calendar({
    version: 'v3',
    auth: oAuth2Client
})

function addAssignment(assignment) {
    calendar.events.insert({
        calendarId: 'primary',
        resource: assignment
    }, err => {
        if (err) return console.error('Calendar Event Creation Error', err)

        return console.log('Calendar Event Created')
    })
}

function listEvents(){
    return calendar.events.list({
        calendarId: 'primary'
    }, (err) => {
        if (err) return console.error(err)
        return ("listed")

    })
}

exports.addAssignment = addAssignment
exports.listEvents = listEvents