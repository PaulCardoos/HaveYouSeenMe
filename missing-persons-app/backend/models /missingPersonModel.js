import { Schema } from 'mongoose';


const missingPersonSchema = new Schema({
    name:{type: String},
    image: {type: String},
    missingSince: {type: String},
    missingFrom:{type: String},
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


const MissingPerson = mongoose.model('MissingPerson', userSchema)

export default MissingPerson