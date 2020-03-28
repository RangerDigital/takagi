from flask import Blueprint

from extensions import rd, db
from helpers import return_json

health = Blueprint("health", __name__)


# Get metrics from service.
@health.route("/health", methods=["GET"])
def get_health():
    payload = {}
    code = 200

    try:
        db.polls.find_one()
        payload["mongo_db"] = "success"
    except: # pylint: disable=W0702
        payload["mongo_db"] = "failure"
        code = 400

    try:
        payload["logins"] = rd.get("counters:logins") or 0
        payload["logins_success"] = rd.get("counters:logins:success") or 0
        payload["logins_failure"] = rd.get("counters:logins:failure") or 0

        payload["polls"] = rd.get("counters:polls") or 0
        payload["votes"] = rd.get("counters:votes") or 0

        payload["redis_db"] = "success"
    except: # pylint: disable=W0702
        payload["redis_db"] = "failure"
        code = 400

    return return_json(payload), code
