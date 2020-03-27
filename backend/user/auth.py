import os
import hashlib

from flask import Blueprint, jsonify
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

from bson.objectid import ObjectId
from marshmallow import Schema, fields

from extensions import db
from helpers import validate_schema, return_error

auth = Blueprint("auth", __name__)


class UpdatePassword(Schema):
    password = fields.String(required=True)


class Auth(Schema):
    email = fields.String(required=True)
    password = fields.String(required=True)


class Register(Schema):
    name = fields.String(required=True)

    email = fields.String(required=True)
    password = fields.String(required=True)


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


# Get JWT token with email and password.
@auth.route("/users/login", methods=["POST"])
@validate_schema(Auth())
def login_user(payload):
    user = db.users.find_one({"email": payload["email"]})

    if not user:
        return return_error("Invalid credentials!", 401)

    password_hash = hashlib.pbkdf2_hmac(
        "sha256", payload["password"].encode("utf-8"), user["salt"], 100000)

    if password_hash != user["password"]:
        return return_error("Invalid credentials!", 401)

    jwt_token = create_access_token(identity=str(user["_id"]))

    return jsonify({"jwt_token": jwt_token}), 200


@auth.route("/users/register", methods=["POST"])
@validate_schema(Register())
def register_user(payload):
    if db.users.find_one({"email": payload["email"]}):
        return return_error("Email address is already in use!", 400)

    user = {}
    user.update(payload)

    user["salt"], user["password"] = generate_hash(payload["password"])

    db.users.insert_one(user)

    return jsonify(""), 204


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

    return jsonify(""), 204
