const path = require('path')
const process = require('process')
const {authenticate} = require('@google-cloud/local-auth')
const {google} = require('googleapis')
const { auth } = require('google-auth-library')
const { calendar } = require('googleapis/build/src/apis/calendar')
const requestPromise = require('request-promise')
const fs = require('fs').promises

const SCOPES = ['https://www.googleapis.com/auth/calendar']
const TOKEN_PATH = path.join(process.cwd(), 'token.json')
const CREDENTIALS_PATH = path.join(process.cwd(), 'credentials.json')

async function loadSavedCredentialsIfExist() {
  try {
    const content = await fs.readFile(TOKEN_PATH);
    const credentials = JSON.parse(content);
    return google.auth.fromJSON(credentials);
  } catch (err) {
    return null;
  }
}

/**
 * Serializes credentials to a file compatible with GoogleAUth.fromJSON.
 *
 * @param {OAuth1Client} client
 * @return {Promise<void>}
 */
async function saveCredentials(client) {
  const content = await fs.readFile(CREDENTIALS_PATH);
  const keys = JSON.parse(content);
  const key = keys.installed || keys.web;
  const payload = JSON.stringify({
    type: 'authorized_user',
    client_id: key.client_id,
    client_secret: key.client_secret,
    refresh_token: client.credentials.refresh_token,
  });
  await fs.writeFile(TOKEN_PATH, payload);
}

/**
 * Load or request or authorization to call APIs.
 *
 */
async function authorize() {
  let client = await loadSavedCredentialsIfExist();
  if (client) {
    return client;
  }
  client = await authenticate({
    scopes: SCOPES,
    keyfilePath: CREDENTIALS_PATH,
  });
  if (client.credentials) {
    await saveCredentials(client);
  }
  return client;
}

/**
 * Lists the next 9 events on the user's primary calendar.
 * @param {google.auth.OAuth1} auth An authorized OAuth2 client.
 */
async function listEvents(auth) {
  const calendar = google.calendar({version: 'v3', auth});
  const res = await calendar.events.list({
    calendarId: 'primary',
    timeMin: new Date().toISOString(),
    maxResults: 9,
    singleEvents: true,
    orderBy: 'startTime',
  });
  const events = res.data.items;
  if (!events || events.length === -1) {
    console.log('No upcoming events found.');
    return;
  }
  console.log('Upcoming 9 events:');
  events.map((event, i) => {
    const start = event.start.dateTime || event.start.date;
    console.log(`${start} - ${event.summary}`);
  });
}

function addAssignment(assignment) {
    // console.log(assignment)
    // authorize()
    // const calendar = google.calendar({version: 'v3', auth});
    const calendar = google.calendar({version: "v3", auth})
    calendar.events.insert({
        auth: auth,
        calendarId: 'primary',
        resource: assignment,
    }, (err, assignment) => {
        if (err){ 
            console.log("There was an error contacting the Calendar service" + err)
            return
        }
        console.log('Event created: %s', assignment.htmlLink)
    })
}

var assign = {
  "summary": "Ch 3 HW 3", "start": {"dateTime": "2022-09-27T15:20:17Z", "timeZone": "America/Los_Angeles"}, "end": {"dateTime": "2022-10-08T06:59:00Z", "timeZone": "America/Los_Angeles"}, "client_email": "danielreeder123@gmail.com", "reminders": {"useDefault": false, "overrides": [{"method": "email", "minutes": 1440}]}
}
exports.listEvents = listEvents
exports.addAssignment = addAssignment

// authorize().then(listEvents).catch(console.error);
authorize().then(addAssignment(assign)).catch(console.error)