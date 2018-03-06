"""
Module containing the generic implementation for a service, which serves as a wrapper
for the RestaurantChooserDatabase object and executes its operations accordingly. Classes that
extend the base class may override the base methods as necessary.
"""

class BaseService(object):
    """
    Base service whose methods merely serve as a wrapper for an existing RestaurantChooserDatabase object's
    methods.
    """

    def __init__(self, table_name):
        """
        Sets the table for which the service is associated with.
        """

        self.table_name = table_name

    def get_all(self, db_obj):
        """
        Gets all items from the database.

        :param db_obj: Database object being used to get the data.

        :return: List of dictionaries for every queried item.
        """

        return db_obj.get_all(self.table_name)

    def get_by_id(self, db_obj, id):
        """
        Gets an item with the given id from the database.

        :param db_obj: Database object being used to get the data.

        :param id: Id of the item being queried.

        :return: Dictionary containing parameters for the queried item.
        """

        return db_obj.get_by_id(self.table_name, id)

    def insert_item(self, db_obj, parameters):
        """ 
        Inserts item with given parameters into the database.

        :param db_obj: Database object being used to get the data.

        :param parameters: Dictionary containing the values to be inserted into the database.

        :return: Dictionary of parameters with database id added.
        """

        return db_obj.insert_item(self.table_name, parameters)

    def update_item(self, db_obj, id, parameters):
        """ 
        Updates item within the database with new parameters.
        
        :param db_obj: Database object being used to get the data.

        :param id: Identifier used to determine which item to update within the database.

        :param parameters: Dictionary containing the column name->value mappings for data to be updated.

        :return: Dictionary containing parameters for the updated item after update.
        """

        return db_obj.update_item(self.table_name, id, parameters)

    def delete_item(self, db_obj, id):
        """
        Deletes item with given id from the table.

        :param db_obj: Database object being used to get the data.

        :param id: Identifier used to determine which item to delete within the database.
        """

        db_obj.delete_item(self.table_name, id)

# Imports the different services into the top level module
from services.user_service import UserService