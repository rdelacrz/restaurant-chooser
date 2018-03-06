"""
This module's methods configure the database connection that will be used for all resource requests.
"""

# Third-party modules
from flask import g

# User-defined modules
from mongo import MongoStorage
from web_api.app import app
from database.restaurant_chooser_database import RestaurantChooserDatabase

def get_db():
    """
    Gets SQLite database instance from local proxy, or initializes new instance if it doesn't exist.
    """

    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = RestaurantChooserDatabase()
    return db

def get_mongo():
    """
    Gets Mongo database instance from local proxy, or initializes new instance if it doesn't exist.
    """

    db = getattr(g, '_mongo', None)
    if db is None:
        db = g._mongo = MongoStorage()
    return db

def close_db_connection(exception):
    """
    Close the SQLite database connection once a request or the application itself is closed.
    """

    db = getattr(g, '_database', None)
    if db is not None:
        db.close_connection()
        g._database = None

def close_mongo_connection(exception):
    """
    Close the Mongo database connection once a request or the application itself is closed.
    """

    db = getattr(g, '_mongo', None)
    if db is not None:
        db.close_connection()
        g._mongo = None

# This location is meant for storing code that disconnects from databases
app.teardown_appcontext_funcs.append(close_db_connection)
app.teardown_appcontext_funcs.append(close_mongo_connection)