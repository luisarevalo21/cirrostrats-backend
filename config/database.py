from pymongo import MongoClient
# import motor.motor_asyncio
from decouple import config
import certifi


client = MongoClient(config('connection_string'), tlsCAFile=certifi.where())


# database name
db = client.cirrostrats

# collection name
collection = db['airports']
