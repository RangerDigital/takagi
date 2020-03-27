from pymongo import MongoClient
from flask_jwt_extended import JWTManager

from config import Configuration


jwt = JWTManager()
config = Configuration()
db = MongoClient(config.MONGO_ADDRESS)[config.MONGO_DATABASE]
