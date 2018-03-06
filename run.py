'''
The main module responsible for running the web browser

@author: Roger Delacruz
'''

#Built-in modules
import os

# User-defined modules
from cmd_parser import ARG_PROD_FLAG, ARG_RESET_DB_FLAG
from database.restaurant_chooser_database import reset_database_structure
from models import RestaurantModel
from web_api.app import app

if __name__ == "__main__":
    if ARG_PROD_FLAG:
        print("Running web application in production mode...")
    else:
        print("Running web application in development mode...")

    if ARG_RESET_DB_FLAG:
        print("Resetting the database content and structure...")
        reset_database_structure()

    app.run(use_reloader=True, debug=True)