import express from 'express'
import dotenv from 'dotenv'
import {Connect} from "./connect.js"
import MissingPerson from './models/missingPersonModel.js'
import searchRoutes from './routes/searchRoutes.js'
const app = express()

dotenv.config()

Connect()
app.use('/api/v1/search', searchRoutes)

app.get('/', (req, res) => {
    res.send("this is money")
})

app.get('/', async (req, res) => {
    //test route for now 
    const record = await MissingPerson.find({firstName : "Paul"})
    res.send(record)
})


app.listen(3000, () => {
    console.log("listening on port 3000")
})


