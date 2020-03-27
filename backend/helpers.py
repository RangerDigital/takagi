from functools import wraps
from flask import jsonify, request

from marshmallow import ValidationError


def return_error(error_msg="Application Error!", status_code=400):
    """Returns JSON error.

    Args:
        msg (Str): Error message.
        code (Int): Status code.

    Returns:
        Response: Flask JSON Response.

    """
    return jsonify({"status": "error", "code": status_code, "msg": error_msg}), status_code


def validate_schema(schema):
    """Validates payload body by Marshmallow schema.

    Args:
        schema (Schema): Marshmallow schema to validate.

    Returns:
        payload: Parsed payload body.

    """
    def decorator(function):

        @wraps(function)
        def wrapper(*args, **kwargs):
            payload = request.get_json(force=True)

            try:
                payload = schema.load(payload)

            except ValidationError as error:
                return return_error(error.messages)

            return function(payload, *args, **kwargs)

        return wrapper
    return decorator
