//this was used to update our data in the database will not be live in production




// import express from 'express'
// import MissingPerson from '../models/missingPersonModel.js'
// const router = express.Router()

// router.get('/', async (req, res) => {
//     const kids = await MissingPerson.find({})
//     let ids = []
//     kids.forEach(element => {
//         ids.push(element._id)
//     });

//     for(let i = 0; i < ids.length; i++){
//         try{

//             const kid = await MissingPerson.findById(ids[i])
//             let location = kid.missingFrom
//             location = location.split(',')
//             let missingFromCity = location[0]
//             let missingFromState = location[1]
//             const updatedKid = await MissingPerson.findByIdAndUpdate(ids[i], {
//                 city : missingFromCity,
//                 state : missingFromState
//             })
    
//             await updatedKid.save()
//         } catch(e){
//             console.log(e)
//         }
        
//     }
// })