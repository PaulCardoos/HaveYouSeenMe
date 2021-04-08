import mongoose from 'mongoose';
const {Schema} = mongoose
const missingPersonSchema = new Schema({
    firstName:{type: String},
    lastName: {type : String},
    image: {type: String},
    missingSince: {type: String},
    missingFrom:{type: String},
    city: {type: String},
    state: {type: String},
    ageNow:{type: Number},
    sex:{type: String},
    race:{type: String},
    hairColor:{type: String},
    eyeColor:{type: String},
    height:{type: String},
    weight:{type: String},
    details:{type: String},
    },
    {collection: 'missingKids'})


const MissingPerson = mongoose.model('MissingPerson', missingPersonSchema, 'missingKids')

export default MissingPerson