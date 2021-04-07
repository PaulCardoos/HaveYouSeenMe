import mongo from 'mongodb'
const {MongoClient} = mongo


export const Connect = async () => {
    let client = new MongoClient(process.env.MONGO_URI, {useUnifiedTopology: true, useNewUrlParser: true})
    client = await client.connect()
    const db = await client.db(process.env.DB)
    const collection = await db.collection(process.env.COLLECTION)
    const kid = await collection.findOne({name: "Alona Allen-Barnes"})
    console.log(kid)

}
