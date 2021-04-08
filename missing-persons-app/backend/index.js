import express from 'express'
import dotenv from 'dotenv'
import {Connect} from "./connect.js"
import searchRoutes from './routes/searchRoutes.js'

//can refer to documentations https://expressjs.com/
const app = express()
dotenv.config()
Connect()

//this api will be used to search for individuals
app.use('/api/v1/search', searchRoutes)

// for parsing application/json
app.use(express.json())

// for parsing application/x-www-form-urlencoded
app.use(express.urlencoded({ extended: true })) 

//test route
app.get('/', (req, res) => {
    res.send("testing")
})

//barebones error handler
app.use((err, req, res, next) => {
    res.send("error")
})

app.listen(3000, () => {
    console.log("listening on port 3000")
})


