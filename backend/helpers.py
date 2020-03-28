import json
from functools import wraps
from flask import request, Response

from bson import ObjectId
from marshmallow import ValidationError


def return_json(payload, status_code=200):
    """Returns JSON response.

    Args:
        payload (Dict): Response payload.
        code (Int): Status code.

    Returns:
        Response: Flask JSON Response.

    """

    # Disable PyLint false positive method-hidden error.
    class JSONEncoder(json.JSONEncoder):
        def default(self, o): # pylint: disable=E0202
            if isinstance(o, ObjectId):
                return str(o)

            return json.JSONEncoder.default(self, o)

    payload = json.dumps(payload, cls=JSONEncoder)

    return Response(response=payload, status=status_code, mimetype="application/json")


def return_error(error_msg="Application Error!", status_code=400):
    """Returns JSON error.

    Args:
        msg (Str): Error message.
        code (Int): Status code.

    Returns:
        Response: Flask JSON Response.

    """
    return return_json({"status": "error", "code": status_code, "msg": error_msg}), status_code


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
