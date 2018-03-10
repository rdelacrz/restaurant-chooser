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
        Inserts user with given parameters into the SQLite database. In addition, if data exists for 
        the file_data parameter, a file is created accordingly within the Mongo database,
        and the mongo id associated with the inserted file is stored within the SQLite database.

        :param sqlite_obj: SQLite database object being used to get the data.
        
        :param mongo_obj: Mongo database object being used to get file data.

        :param parameters: Dictionary containing the values to be inserted into the database.

        :return: Dictionary of parameters with database id added.
        """
        
        # Adds file data to the Mongo database
        file_data = UserService.get_file_data(parameters)
        if (file_data):
            parameters["image_mongo_id"] = mongo_obj.add_file_data(file_data.parameters)

        parameters.pop("file_data", None)
        return sqlite_obj.insert_item(self.table_name, parameters)

    def update_item(self, sqlite_obj, mongo_obj, id, parameters):
        """ 
        Updates user within the database with new parameters.
        
        :param sqlite_obj: Database object being used to get the data.

        :param mongo_obj: Mongo database object being used to get file data.
        
        :param id: Identifier used to determine which item to update within the database.

        :param parameters: Dictionary containing the column name->value mappings for data to be updated.

        :return: Dictionary containing parameters for the updated item after update.
        """

        # Updates file data within the Mongo database, if new file data exists
        file_data = UserService.get_file_data(parameters)
        if (file_data):
            parameters["image_mongo_id"] = mongo_obj.add_file_data(file_data.parameters)

        parameters.pop("file_data", None)
        return sqlite_obj.update_item(self.table_name, id, parameters)

    @classmethod
    def get_file_data(cls, user_data):
        """
        Get file data object that will be used to either insert or update a file within MongoDB.

        :param user_data: User data object with information about potential file data.

        :return: File data dictionary generated using the parameters of the user data object.
        """

        user = FullUserDataModel(**user_data)

        # Builds file data dictionary if file data exists within given user data
        if (user.file_data != None):
            file_data = FileDataModel(**user.file_data)

             # Renames the file using the user full name and file type
            file_name = user.first_name + "_" + user.last_name
            if "jpeg" in file_data.file_type:
                file_name = file_name + ".jpg"
            elif "png" in file_data.file_type:
                file_name = file_name + ".png"
            else:
                raise Exception("Invalid image file type passed for uploaded image.")
            file_data.file_name = file_name

            return file_data
        else:
            return None