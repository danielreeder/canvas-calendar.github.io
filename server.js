if (process.env.NODE_ENV !== 'production'){
    require('dotenv').config
}

const CANVAS_API_KEY = process.env.CANVAS_API_KEY
const express = require('express')
const app = express()

app.use(express.json())
app.use(express.static('public'))

app.post('/calendar', (req, res) => {

})

app.listen(3000, () => {
    console.log('Server has started')
})
