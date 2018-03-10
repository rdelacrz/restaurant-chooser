"""
This module is responsible for running the application's Flask-based REST API. 
"""

from web_api.app import app

REST_CMD = "python rest.py"

if __name__ == "__main__":
    app.run(use_reloader=True, debug=True)