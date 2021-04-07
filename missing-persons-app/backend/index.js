
import express from 'express'
import dotenv from 'dotenv'

const app = express()

dotenv.config({path: ".env"})

app.get('/', (req, res) => {
    res.send("this is money")
})

app.listen(3000, () => {
    console.log("listening on port 3000")
})
console.log(process.env.MONGO_URI)

