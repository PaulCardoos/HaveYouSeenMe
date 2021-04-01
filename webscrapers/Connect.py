import os 
import pymongo
from dotenv import load_dotenv
from pathlib import Path 
 
env_path = Path('..') / '.env'
load_dotenv(dotenv_path=env_path)
MONGO_URI = os.getenv("MONGO_URI")
DB = os.getenv("DB")
COLLECTION =os.getenv("COLLECTION")

def connect():
    client = pymongo.MongoClient(MONGO_URI)
    db = client[DB]
    collection = db[COLLECTION]
    return collection

connect()
