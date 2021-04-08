import mongoose from 'mongoose'



export const Connect = async () => {
   try{
       const connection = await mongoose.connect(process.env.MONGO_URI, {
           useNewUrlParser : true,
           useUnifiedTopology : true,
           useCreateIndex : true
       })

       console.log("Mongo DB connected")
   } catch (error) {
       console.log("connection failed")
   }
}