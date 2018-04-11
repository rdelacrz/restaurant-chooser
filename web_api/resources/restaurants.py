"""
This module contains resources for every restaurant-related REST operation.
"""

# Third-party modules
from flask import jsonify
from flask_restful import Resource, reqparse

# User-defined modules
from services import RestaurantService
from web_api.common.choices import state_ids
from web_api.common.validators import phone_number, zip_code
from web_api.resources import get_db

# Defines the POST parser
post_parser = reqparse.RequestParser(bundle_errors=True)
post_parser.add_argument("name", type=str, required=True)
post_parser.add_argument("cuisine_type_id", type=int, required=True)
post_parser.add_argument("address_line", type=str)
post_parser.add_argument("city", type=str)
post_parser.add_argument("state_id", type=int, choices=state_ids)
post_parser.add_argument("zip", type=zip_code)
post_parser.add_argument("phone_number", type=phone_number)
post_parser.add_argument("suggester_id", type=int, required=True)
post_parser.add_argument("schedule_items", type=list)

# Defines the PUT parser
put_parser = reqparse.RequestParser(bundle_errors=True)
put_parser.add_argument("name", type=str, store_missing=False)
put_parser.add_argument("cuisine_type_id", type=int, store_missing=False)
put_parser.add_argument("address_line", type=str, store_missing=False)
put_parser.add_argument("city", type=str, store_missing=False)
put_parser.add_argument("state_id", type=int, choices=state_ids, store_missing=False)
put_parser.add_argument("zip", type=zip_code, store_missing=False)
put_parser.add_argument("phone_number", type=phone_number, store_missing=False)
put_parser.add_argument("suggester_id", type=int, store_missing=False)
put_parser.add_argument("schedule_items", type=list, store_missing=False)

class RestaurantBase(Resource):
    def get(self):
        return jsonify(get_db().get_all("restaurants"))

    def post(self):
        args = post_parser.parse_args()
        return jsonify(RestaurantService().insert_item(get_db(), args))

class RestaurantItem(Resource):
    def get(self, id):
        return jsonify(get_db().get_by_id("restaurants", id))

    def put(self, id):
        args = put_parser.parse_args()
        return get_db().update_item("restaurants", id, args)

    def delete(self, id):
        get_db().delete_item("restaurants", id)
        return jsonify({"message":"Restaurant with id={} has been deleted.".format(id)})
    
