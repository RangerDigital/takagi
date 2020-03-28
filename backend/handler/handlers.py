from flask import Blueprint

from extensions import jwt, rd
from helpers import return_error

handlers = Blueprint("handlers", __name__)


@handlers.app_errorhandler(400)
@handlers.app_errorhandler(404)
@handlers.app_errorhandler(405)
@handlers.app_errorhandler(500)
def error_handler(error):
    return return_error(error.description, error.code)


@handlers.app_errorhandler(429)
def limit_handler(error):
    rd.incr("counters:limit_hit")
    return return_error("Too many requests! Limit: " + error.description, error.code)


@jwt.expired_token_loader
def expired_error(expired_token):
    return return_error("The {} token has expired!".format(expired_token["type"]), 401)


@jwt.unauthorized_loader
def unauthorized_error(error):
    return return_error(error, 401)
