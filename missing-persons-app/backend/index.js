import express from 'express'
import dotenv from 'dotenv'
import {Connect} from "./connect.js"
const app = express()

dotenv.config()

const kids = Connect()


app.get('/', (req, res) => {
    res.send("this is money")
})

app.get('/find/name', async (req, res) => {
    //test route for now 
    
})


app.listen(3000, () => {
    console.log("listening on port 3000")
})


