import time

from flask import Blueprint, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_optional, jwt_required

from bson.objectid import ObjectId
from marshmallow import Schema, fields

from extensions import db
from helpers import validate_schema, return_error, return_json

polls = Blueprint("polls", __name__)


class Poll(Schema):
    question = fields.String(required=True)
    options = fields.List(fields.String(), required=True)


class Vote(Schema):
    option_id = fields.Int(required=True)
    fingerprint = fields.String(required=True)


# Create new poll.
@polls.route("/polls", methods=["POST"])
@jwt_optional
@validate_schema(Poll())
def create_poll(payload):
    user_id = get_jwt_identity()
    poll = {}

    # Tag poll if user is logged.
    if user_id:
        poll["_user_id"] = user_id
        poll["name"] = db.users.find_one({"_id":  ObjectId(user_id)})["name"]
    else:
        poll["name"] = "Anonymous"

    poll["voters"] = []
    poll["created_at"] = time.time()
    poll["question"] = payload["question"]

    # Prepare options database scheme.
    poll["options"] = []
    for option in payload["options"]:
        poll["options"].append({"name": option, "votes": 0})

    db.polls.insert_one(poll)

    return return_json(poll), 201


# Get all polls from logged user.
@polls.route("/polls", methods=["GET"])
@jwt_required
def get_polls():
    user_id = get_jwt_identity()

    user_polls = []
    for poll in db.polls.find({"_user_id": user_id}):
        user_polls.append(poll)

    return return_json(user_polls), 200


# Get poll by ID.
@polls.route("/polls/<poll_id>", methods=["GET"])
def get_poll(poll_id):

    if not ObjectId.is_valid(poll_id):
        return return_error("Invalid ID format!")

    poll = db.polls.find_one({"_id": ObjectId(poll_id)})
    if not poll:
        return return_error("Poll with that Id not found!", 404)

    return return_json(poll), 200


# Delete poll created by logged user.
@polls.route("/polls/<poll_id>", methods=["DELETE"])
@jwt_required
def delete_poll(poll_id):
    user_id = ObjectId(get_jwt_identity())

    if not ObjectId.is_valid(poll_id):
        return return_error("Invalid ID format!")

    db.polls.delete_one({"_id": ObjectId(poll_id), "_user_id": user_id})

    return return_json(""), 204


# Vote in public poll once.
@polls.route("/polls/<poll_id>/vote", methods=["POST"])
@validate_schema(Vote())
def vote_poll(payload, poll_id):
    if not ObjectId.is_valid(poll_id):
        return return_error("Invalid ID format!")

    poll = db.polls.find_one({"_id": ObjectId(poll_id)})

    if not poll:
        return return_error("Poll not found!", 404)

    # Check if user fingerprint already in database.
    if payload["fingerprint"] in poll["voters"]:
        return return_error("You already voted in that poll!")

    poll["voters"].append(payload["fingerprint"])
    poll["options"][payload["option_id"]]["votes"] += 1

    db.polls.replace_one({"_id": ObjectId(poll_id)}, poll)

    return return_json(poll), 201
