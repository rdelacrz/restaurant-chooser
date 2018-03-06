"""
This module contains the service used to perform user-related operations. All functions defined here
will override the functions defined in the base service.
"""

# Built-in modules
import base64
from os.path import join

# User-defined modules
from config import DATA_DIR, IMAGES_FOLDER
from services import BaseService
from view_models import FileDataModel, FullUserDataModel

# Path to the images folder where user image files will be saved
_IMAGES_PATH = join(DATA_DIR, IMAGES_FOLDER)

class UserService(BaseService):
    """
    Service specialized for user operations.
    """

    def __init__(self):
        super().__init__("users")

    def get_all(self, sqlite_obj, mongo_obj):
        """
        Gets all users from the database. If an associated user has an image file linked to him/her,
        the file data is sent along with the user data.

        :param sqlite_obj: SQLite database object being used to get the data.

        :param mongo_obj: Mongo database object being used to get file data.

        :return: List of dictionaries for every queried item.
        """

        data_list = []

        # Gets user data from the database and gets file data as necessary
        for user in sqlite_obj.get_all(self.table_name):
            image_mongo_id = user.pop('image_mongo_id')
            user['file_data'] = mongo_obj.get_file_data(image_mongo_id) if (image_mongo_id) else None
            data_list.append(user)

        return data_list

    def get_by_id(self, sqlite_obj, mongo_obj, id):
        """
        Gets a user with the given id from the database. If the user has an image file linked to 
        him/her, the file data is sent along with the user data.

        :param sqlite_obj: SQLite database object being used to get the data.
        
        :param mongo_obj: Mongo database object being used to get file data.

        :param id: Id of the user being queried.

        :return: Dictionary containing parameters for the queried item.
        """

        user = sqlite_obj.get_by_id(self.table_name, id)
        image_mongo_id = user.pop('image_mongo_id')
        user['file_data'] = mongo_obj.get_file_data(image_mongo_id) if (image_mongo_id) else None
        return user

    def insert_item(self, sqlite_obj, mongo_obj, parameters):
        """ 
        Inserts item with given parameters into the SQLite database. In addition, if data exists for 
        the file_data parameter, a file is created accordingly within the Mongo database,
        and the mongo id associated with the inserted file is stored within the SQLite database.

        :param sqlite_obj: SQLite database object being used to get the data.
        
        :param mongo_obj: Mongo database object being used to get file data.

        :param parameters: Dictionary containing the values to be inserted into the database.

        :return: Dictionary of parameters with database id added.
        """

        add_user = FullUserDataModel(**parameters)

        # Creates a new image file for the given user if file data exists
        if (add_user.file_data != None):
            file_data = FileDataModel(**add_user.file_data)

             # Renames the file using the user full name and file type
            file_name = add_user.first_name + "_" + add_user.last_name
            if "jpeg" in file_data.file_type:
                file_name = file_name + ".jpg"
            elif "png" in file_data.file_type:
                file_name = file_name + ".png"
            else:
                raise Exception("Invalid image file type passed for uploaded image.")
            file_data.file_name = file_name

            # Adds file data to the Mongo database
            parameters["image_mongo_id"] = mongo_obj.add_file_data(file_data.parameters)

        parameters.pop("file_data", None)
        return sqlite_obj.insert_item(self.table_name, parameters)