from flask import Blueprint

from extensions import rd, db, limiter
from helpers import return_json

health = Blueprint("health", __name__)


# Get metrics from service.
@health.route("/health", methods=["GET"])
@limiter.limit("100/minute")
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

        payload["limit_hit"] = rd.get("counters:limit_hit") or 0

        payload["redis_db"] = "success"
    except: # pylint: disable=W0702
        payload["redis_db"] = "failure"
        code = 503

    return return_json(payload), code
