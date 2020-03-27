from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from bson.objectid import ObjectId
from marshmallow import Schema, fields

from extensions import db
from helpers import validate_schema, return_error

users = Blueprint("users", __name__)


class User(Schema):
    name = fields.String()
    email = fields.String()


# Get info about logged user.
@users.route("/users/me", methods=["GET"])
@jwt_required
def get_logged_user():
    user = db.users.find_one({"_id":  ObjectId(get_jwt_identity())}, {"password": 0, "salt": 0})

    if not user:
        return return_error("User with that Id not found!", 404)

    user["_id"] = str(user["_id"])

    return jsonify(user)


# Update info about logged user.
@users.route("/users/me", methods=["PATCH"])
@jwt_required
@validate_schema(User())
def update_logged_user(payload):
    user_id = ObjectId(get_jwt_identity())
    user = db.users.find_one({"_id":  user_id})

    # Check if Email is already used.
    if db.users.find_one({"_id": {"$ne": user_id}, "email": payload.get("email"), "initiated": True}):
        return return_error("Email address is already in use!", 400)

    user.update(payload)
    db.users.replace_one({"_id": user_id}, user)

    user["_id"] = str(user["_id"])

    del user["salt"]
    del user["password"]

    return jsonify(user)
