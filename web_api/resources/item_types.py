"""
This module contains resources for every item type-related REST operation.
"""

# Third-party modules
from flask import jsonify
from flask_restful import Resource, reqparse

# User-defined modules
from web_api.resources import get_db
from database.restaurant_chooser_database import RestaurantChooserDatabase

# Defines the POST parser
post_parser = reqparse.RequestParser(bundle_errors=True)
post_parser.add_argument("item_type", type=str, required=True)

# Defines the PUT parser
put_parser = reqparse.RequestParser(bundle_errors=True)
put_parser.add_argument("item_type", type=str, required=True)

class ItemTypeBase(Resource):
    def get(self):
        return jsonify(get_db().get_all("item_types"))

    def post(self):
        args = post_parser.parse_args()
        return jsonify(get_db().insert_item("item_types",args))

class ItemTypeItem(Resource):
    def get(self, id):
        return jsonify(get_db().get_by_id("item_types", id))

    def put(self, id):
        args = put_parser.parse_args()
        return get_db().update_item("item_types", id, args)

    def delete(self, id):
        get_db().delete_item("item_types", id)
        return jsonify({"message":"Item type with id={} has been deleted.".format(id)})
    
