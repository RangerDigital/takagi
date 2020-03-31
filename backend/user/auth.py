import os
import hashlib

from flask import Blueprint
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

from bson.objectid import ObjectId
from marshmallow import Schema, fields, validate

from extensions import db, rd, limiter
from helpers import validate_schema, return_error, return_json

auth = Blueprint("auth", __name__)


class UpdatePassword(Schema):
    password = fields.String(required=True, validate=validate.Length(min=8))


class Auth(Schema):
    email = fields.String(required=True)
    password = fields.String(required=True, validate=validate.Length(min=8))


class Register(Schema):
    name = fields.String(required=True, validate=validate.Length(min=1, max=15))

    email = fields.String(required=True)
    password = fields.String(required=True, validate=validate.Length(min=8))


def generate_hash(password):
    """Generate user hash, salt.

    Args:
        password (Str): User password.

    Returns:
        salt: Salt generated with hash.
        password_hash: Hashed user password.

    """
    salt = os.urandom(32)
    password_hash = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100000)

    return salt, password_hash


# Get JWT token from email and password.
@auth.route("/users/login", methods=["POST"])
@limiter.limit("500/day;50/minute")
@validate_schema(Auth())
def login_user(payload):
    rd.incr("counters:logins")
    user = db.users.find_one({"email": payload["email"]})

    if not user:
        rd.incr("counters:logins:failure")
        return return_error("Invalid credentials!", 401)

    password_hash = hashlib.pbkdf2_hmac(
        "sha256", payload["password"].encode("utf-8"), user["salt"], 100000)

    if password_hash != user["password"]:
        rd.incr("counters:logins:failure")
        return return_error("Invalid credentials!", 401)

    jwt_token = create_access_token(identity=str(user["_id"]))

    rd.incr("counters:logins:success")
    return return_json({"jwt_token": jwt_token}), 200


# Create new user.
@auth.route("/users/register", methods=["POST"])
@limiter.limit("250/day;25/minute")
@validate_schema(Register())
def register_user(payload):
    if db.users.find_one({"email": payload["email"]}):
        return return_error("Email address is already in use!", 400)

    payload["salt"], payload["password"] = generate_hash(payload["password"])

    db.users.insert_one(payload)

    rd.incr("counters:registers:success")
    return return_json(""), 204


# Update password for logged user.
@auth.route("/users/me/password", methods=["POST"])
@jwt_required
@validate_schema(UpdatePassword())
def update_password(payload):
    user_id = ObjectId(get_jwt_identity())
    user = db.users.find_one({"_id":  user_id})

    if not user:
        return return_error("User not found!", 404)

    user["salt"], user["password"] = generate_hash(payload["password"])

    db.users.replace_one({"_id": user["_id"]}, user)

    return return_json(""), 204
