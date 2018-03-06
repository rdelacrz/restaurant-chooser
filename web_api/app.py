"""
This module contains the Flask application and defines the URL routing.
"""

# Built-in modules
from os.path import join

# Third-party modules
from flask import Flask, redirect, request
from flask_restful import Api

# User-defined modules
from cmd_parser import ARG_PROD_FLAG
from config import DEV_APP_DIR, PROD_APP_DIR
from utilities import get_base_path

# Establishes routes to the static web files
WEB_APP_PATH = None
if ARG_PROD_FLAG:
    WEB_APP_PATH = join(get_base_path(), PROD_APP_DIR)
else:
    WEB_APP_PATH = join(get_base_path(), DEV_APP_DIR)

# Initializes the application and API (must be defined before resource imports)
app = Flask(__name__, static_folder=WEB_APP_PATH, static_url_path="")
api = Api(app)

# User-defined modules
from web_api.resources.cuisine_types import CuisineTypeBase, CuisineTypeItem
from web_api.resources.item_types import ItemTypeBase, ItemTypeItem
from web_api.resources.list_items import ListItemBase, ListItemItem, StateBase, WeekdayBase
from web_api.resources.restaurants import RestaurantBase, RestaurantItem
from web_api.resources.schedules import ScheduleBase, ScheduleItem
from web_api.resources.users import UserBase, UserItem

# Establishes routes to all the resources
api.add_resource(CuisineTypeBase, "/api/cuisinetypes")
api.add_resource(CuisineTypeItem, "/api/cuisinetypes/<int:id>")
api.add_resource(ItemTypeBase, "/api/itemtypes")
api.add_resource(ItemTypeItem, "/api/itemtypes/<int:id>")
api.add_resource(ListItemBase, "/api/listitems")
api.add_resource(ListItemItem, "/api/listitems/<int:id>")
api.add_resource(StateBase, "/api/listitems/states")
api.add_resource(WeekdayBase, "/api/listitems/weekdays")
api.add_resource(RestaurantBase, "/api/restaurants")
api.add_resource(RestaurantItem, "/api/restaurants/<int:id>")
api.add_resource(ScheduleBase, "/api/schedules")
api.add_resource(ScheduleItem, "/api/schedules/<int:id>")
api.add_resource(UserBase, "/api/users")
api.add_resource(UserItem, "/api/users/<int:id>")

# Sets response headers to include "Access-Control-Allow-Origin : http://localhost:4200"
def _add_headers_api_requests(response):
    """
    Adds an Access-Control-Allow-Origin: * HTTP header to the response to allow API access from 
    the frontend development server.
    """
    if request.path:
        response.headers.add('Access-Control-Allow-Origin', 'http://localhost:4200')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    return response
app.after_request(_add_headers_api_requests)

@app.route("/")
def root():
    return app.send_static_file("index.html")
