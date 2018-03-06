"""
This module contains resources for every cuisine type-related REST operation.
"""

# Third-party modules
from flask import jsonify
from flask_restful import Resource, reqparse

# User-defined modules
from web_api.resources import get_db
from database.restaurant_chooser_database import RestaurantChooserDatabase

# Defines the POST parser
post_parser = reqparse.RequestParser(bundle_errors=True)
post_parser.add_argument("cuisine_type", type=str, required=True)

# Defines the PUT parser
put_parser = reqparse.RequestParser(bundle_errors=True)
put_parser.add_argument("cuisine_type", type=str, required=True)

class CuisineTypeBase(Resource):
    def get(self):
        return jsonify(get_db().get_all("cuisine_types"))

    def post(self):
        args = post_parser.parse_args()
        return jsonify(get_db().insert_item("cuisine_types", args))

class CuisineTypeItem(Resource):
    def get(self, id):
        return jsonify(get_db().get_by_id("cuisine_types", id))

    def put(self, id):
        args = put_parser.parse_args()
        return get_db().update_item("cuisine_types", id, args)

    def delete(self, id):
        get_db().delete_item("cuisine_types", id)
        return jsonify({"message":"Cuisine type with id={} has been deleted.".format(id)})
    
