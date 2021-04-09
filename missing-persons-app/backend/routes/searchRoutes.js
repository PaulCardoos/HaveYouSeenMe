import express from 'express'
import MissingPerson from '../models/missingPersonModel.js'
const router = express.Router()

//just to get missing kids by state
router.get('/:state', async (req, res) => {
    let { state } = req.params
    //split on a comma leaving an extra whitespace in the DB
    let st = " " + state
    let kids = await MissingPerson.find({state : st})
    res.send(kids)
})


//post for advanced search
router.post('/find', async (req, res) => { 
    const missingPerson = await MissingPerson.find(req.query)
    res.send(missingPerson)
})

export default router