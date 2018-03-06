"""
This module contains resources for every schedule-related REST operation.
"""

# Third-party modules
from flask import jsonify
from flask_restful import Resource, reqparse

# User-defined modules
from web_api.common.choices import weekday_ids
from web_api.common.validators import time
from web_api.resources import get_db

# Defines the POST parser
post_parser = reqparse.RequestParser(bundle_errors=True)
post_parser.add_argument("restaurant_id", type=int, required=True)
post_parser.add_argument("weekday_id", type=int, choices=weekday_ids, required=True)
post_parser.add_argument("opening_time", type=time, required=True)
post_parser.add_argument("closing_time", type=time, required=True)

# Defines the PUT parser
put_parser = reqparse.RequestParser(bundle_errors=True)
put_parser.add_argument("restaurant_id", type=int, store_missing=False)
put_parser.add_argument("weekday_id", type=int, choices=weekday_ids, store_missing=False)
put_parser.add_argument("opening_time", type=time, store_missing=False)
put_parser.add_argument("closing_time", type=time, store_missing=False)

class ScheduleBase(Resource):
    def get(self):
        return jsonify(get_db().get_all("schedules"))

    def post(self):
        args = post_parser.parse_args()
        return jsonify(get_db().insert_item("schedules", args))

class ScheduleItem(Resource):
    def get(self, id):
        return jsonify(get_db().get_by_id("schedules", id))

    def put(self, id):
        args = put_parser.parse_args()
        return get_db().update_item("schedules", id, args)

    def delete(self, id):
        get_db().delete_item("schedules", id)
        return jsonify({"message":"Schedule with id={} has been deleted.".format(id)})
    
