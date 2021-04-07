
import express from 'express'
import dotenv from 'dotenv'
import path from 'path'
const app = express()

dotenv.config()


app.get('/', (req, res) => {
    res.send("this is money")
})

app.listen(3000, () => {
    console.log("listening on port 3000")
})

