import express from 'express'
import MissingPerson from '../models/missingPersonModel.js'
const router = express.Router()


router.get('/:state', async (req, res) => {
    let { state } = req.params
    let st = " " + state
    let kids = await MissingPerson.find({state : st})
    res.send(kids)
})

export default router