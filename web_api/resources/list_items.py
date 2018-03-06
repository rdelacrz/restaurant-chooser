"""
This module contains resources for every list item-related REST operation.
"""

# Third-party modules
from flask import jsonify
from flask_restful import Resource, reqparse

# User-defined modules
from web_api.resources import get_db
from database.restaurant_chooser_database import RestaurantChooserDatabase

# Defines the POST parser
post_parser = reqparse.RequestParser(bundle_errors=True)
post_parser.add_argument("item_id", type=int, required=True)
post_parser.add_argument("item_name", type=str, required=True)
post_parser.add_argument("item_abbreviation", type=str)
post_parser.add_argument("item_type_id", type=int, required=True)

# Defines the PUT parser
put_parser = reqparse.RequestParser(bundle_errors=True)
put_parser.add_argument("item_id", type=int, store_missing=False)
put_parser.add_argument("item_name", type=str, store_missing=False)
put_parser.add_argument("item_abbreviation", type=str, store_missing=False)
put_parser.add_argument("item_type_id", type=int, store_missing=False)

class ListItemBase(Resource):
    def get(self):
        return jsonify(get_db().get_all("list_items"))

    def post(self):
        args = post_parser.parse_args()
        return jsonify(get_db().insert_item("list_items", args))

class ListItemItem(Resource):
    def get(self, id):
        return jsonify(get_db().get_by_id("list_items", id))

    def put(self, id):
        args = put_parser.parse_args()
        return get_db().update_item("list_items", id, args)

    def delete(self, id):
        get_db().delete_item("list_items", id)
        return jsonify({"message":"Item list with id={} has been deleted.".format(id)})
    
class StateBase(Resource):
    def get(self):
        return jsonify(get_db().get_states())

class WeekdayBase(Resource):
    def get(self):
        return jsonify(get_db().get_weekdays())
