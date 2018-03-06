"""
This module is used to read parameters from the config.json file.
"""

# Built-in modules
from json import load

# Constants
CONFIG_PATH = "config.json"

# Modify these functions accordingly whenever the config.json file is modified
def _get_configuration():
    """ Extracts the configuration data from the config.json file. """
    with open(CONFIG_PATH, "r") as file:
        return load(file)

def _get_database_name(key="database"):
    """ Gets the name of the database. """
    return _config_param[key]

def _get_data_directory(key="dataDirectory"):
    """ Gets the relative path to the data directory. """
    return _config_param[key]

def _get_images_folder_name(key="imagesFolder"):
    """ Gets the name of the images folder. """
    return _config_param[key]

def _get_mongo_database_name(key="mongoDatabase"):
    """ Gets the name of the mongo database. """
    return _config_param[key]

def _get_mongo_executable_path(key="mongoExePath"):
    """ Gets the name of the mongo db application executable. """
    return _config_param[key]

def _get_app_directory(key="appEnvironment", isProd=False):
    """ Gets the relative path to the root directory containing the static web files. """
    environment = "production" if isProd else "development"
    return _config_param[key][environment]

# Runs on module initialization
_config_param = _get_configuration()

# Loads configuration variables
DB_NAME = _get_database_name()
DATA_DIR = _get_data_directory()
IMAGES_FOLDER = _get_images_folder_name()
MONGO_DB_NAME = _get_mongo_database_name()
MONGO_EXE_PATH = _get_mongo_executable_path()
DEV_APP_DIR = _get_app_directory()
PROD_APP_DIR = _get_app_directory(isProd=True)