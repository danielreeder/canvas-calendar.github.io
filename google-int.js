const res = require('express/lib/response')
const { google } = require('googleapis')
const { OAuth2 } = google.auth
require('dotenv').config()
const fs = require('fs')
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
        if (err) {
            if (err = ' GaxiosError: The requested identifier already exists'){
                calendar.events.update({
                    calendarId: 'primary',
                    eventId: assignment.id,
                    resource: assignment
                })
                return console.log("Calendar Event Updated")
            }
            return console.error('Calendar Event Creation Error', err)
        }

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

function removeAssignment(assignment) {
    assignment.status = "cancelled"
    calendar.events.delete({
        calendarId: 'primary',
        eventId: assignment.id
    }, err => {
        if (err) {
            return console.err(err)
        }
    })
    return console.log('Calendar Event semoved')
}

exports.addAssignment = addAssignment
exports.listEvents = listEvents
exports.removeAssignment = removeAssignment