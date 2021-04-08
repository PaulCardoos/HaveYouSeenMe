import express from 'express'
import MissingPerson from '../models/missingPersonModel.js'
const router = express.Router()


router.get('/', async (req, res) => {
    const kid = await MissingPerson.findOne({missingFrom : "Boston, MA"})
    console.log(kid)
    res.send(kid)
})

export default router