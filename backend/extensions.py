from redis import Redis
from pymongo import MongoClient
from flask_jwt_extended import JWTManager

from flask_limiter import Limiter
from flask_limiter.util import get_ipaddr

from config import Configuration


jwt = JWTManager()
config = Configuration()
limiter = Limiter(key_func=get_ipaddr, in_memory_fallback_enabled=True, storage_uri="redis://{}:6379".format(config.REDIS_ADDRESS))

db = MongoClient(config.MONGO_ADDRESS)[config.MONGO_DATABASE]
rd = Redis(host=config.REDIS_ADDRESS, decode_responses=True)
