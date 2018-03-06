"""
This module contains methods for accessing and dealing with MongoDB, which is a NoSQL database
that will be used to store file data up to 16 MB.
"""

# Built-in modules
import os
import subprocess

# Third-party modules
from bson.objectid import ObjectId
from pymongo import MongoClient

# User-defined modules
from config import DATA_DIR, MONGO_DB_NAME, MONGO_EXE_PATH
from utilities import get_base_path

# Collection names for the Mongo database
FILE_COLLECTION = "files"

class MongoStorage(object):
    """
    Wrapper used to access MongoDB for file storing purposes.
    """

    def __init__(self):
        self.create_connection()

    def create_connection(self):
        """
        Establishes connection to the Mongo database.
        """

        self.client = MongoClient()     # Default client for Mongo
        self.db = self.client.get_database(MONGO_DB_NAME)
        self.file_collection = self.db.get_collection(FILE_COLLECTION)

    def add_file_data(self, data):
        """
        Adds file data to the file collection.

        :param data: Dictionary containing file data to be inserted.

        :return: Object id associated with the insert.
        """

        return str(self.file_collection.insert_one(data).inserted_id)

    def get_file_data(self, object_id):
        """
        Gets the file data within the file collection using the given object id.

        :param object_id: Object id associated with the file data.

        :return: Data dictionary containing the file data information.
        """

        # Performs query for item
        collection_filter = { "_id" : ObjectId(object_id) }
        file_data = self.file_collection.find_one(collection_filter)

        # Removes id from dictionary - it is not needed
        if (file_data):
            file_data.pop("_id")

        return file_data

    def delete_file_data(self, object_id):
        """
        Deletes the file data within the file collection using the given object id.

        :param object_id: Object id associated with the file data.
        """

        # Performs query for item and deletes it
        collection_filter = { "_id" : ObjectId(object_id) }
        self.file_collection.delete_one(collection_filter)

    def drop_database(self):
        """
        Drops the Mongo database, if it exists.
        """

        self.client.drop_database(MONGO_DB_NAME)

    def close_connection(self):
        """
        Closes the current connection to the Mongo database in order to free up resources.
        """

        self.client.close()

# Run this file directly within a terminal to run the Mongo DB 
if __name__=='__main__':
    mongo_db_path = os.path.join(get_base_path(), DATA_DIR, MONGO_DB_NAME)
    cmd = '"{0}" --dbpath "{1}"'.format(MONGO_EXE_PATH, mongo_db_path)
    subprocess.call(cmd)