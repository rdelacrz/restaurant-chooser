"""
This module contains resources for every user-related REST operation.
"""

# Third-party modules
from flask import jsonify
from flask_restful import Resource, reqparse

# User-defined modules
from services import UserService
from web_api.resources import get_db, get_mongo

# Defines the POST parser
post_parser = reqparse.RequestParser(bundle_errors=True)
post_parser.add_argument("first_name", type=str, required=True)
post_parser.add_argument("middle_name", type=str)
post_parser.add_argument("last_name", type=str, required=True)
post_parser.add_argument("preferences_desc", type=str)
post_parser.add_argument("file_data", type=dict)

# Defines the PUT parser
put_parser = reqparse.RequestParser(bundle_errors=True)
put_parser.add_argument("first_name", type=str, store_missing=False)
put_parser.add_argument("middle_name", type=str, store_missing=False)
put_parser.add_argument("last_name", type=str, store_missing=False)
put_parser.add_argument("preferences_desc", type=str, store_missing=False)
put_parser.add_argument("file_data", type=dict, store_missing=False)

class UserBase(Resource):
    def get(self):
        return jsonify(UserService().get_all(get_db(), get_mongo()))

    def post(self):
        args = post_parser.parse_args()
        return jsonify(UserService().insert_item(get_db(), get_mongo(), args))

class UserItem(Resource):
    def get(self, id):
        return jsonify(UserService().get_by_id(get_db(), get_mongo(), id))

    def put(self, id):
        args = put_parser.parse_args()
        return jsonify(UserService().update_item(get_db(), id, args))

    def delete(self, id):
        UserService().delete_item(get_db(), id)
        return jsonify({"message":"User with id={} has been deleted.".format(id)})
    
