import express from 'express'
import MissingPerson from '../models/missingPersonModel.js'
const router = express.Router()


//post for advanced search
router.post('/find', async (req, res) => { 
    const missingPerson = await MissingPerson.find(req.query)
    console.log(missingPerson.length)
    res.send(missingPerson)
})

//just to get missing kids by state
router.get('/:state', async (req, res) => {
    let { state } = req.params
    //split on a comma leaving an extra whitespace in the DB
    let st = " " + state
    let kids = await MissingPerson.find({state : st})
    res.send(kids)
})

export default router