"""
Module responsible for generating the database structure specific to the Restaurant Chooser application and
accessing its data.
"""

# Built-in modules
from os import remove

# User-defined modules
from database import DatabaseAccessor
from database._restaurant_chooser_init import CREATE_TABLES, INITIAL_VALUE_INSERTS, STATE_ITEM_TYPE, WEEKDAY_ITEM_TYPE
from models import CuisineTypeModel, ItemTypeModel, ListItemModel, RestaurantModel, ScheduleModel, UserModel
from utilities import clear_data

class RestaurantChooserDatabase(object):
    def __init__(self, init_db=False):
        """
        Initializes the Restaurant Chooser Database object, which allows a user to interact with the
        database associated with the application.

        :param init_db: If true, the database will be deleted and then recreated with the default values set. 
        Set to False by default.
        """

        self._db = DatabaseAccessor()

        if (init_db):
            clear_data()    # Clears all data from the app data directory, including the database file

        self._db.create_connection()    # Creates a new database file if it doesn't exist)

        if (init_db):
            self._generate_initial_database_structure()
    
    def _generate_initial_database_structure(self):
        """ Creates the database tables and inserts the initial default values into them. """

        # Generates tables for database if they do not already exist
        for create_table_sql in CREATE_TABLES:
            self._db.execute(create_table_sql)

        # Inserts the default table values
        for insert_sql in INITIAL_VALUE_INSERTS:
            self._db._write_query(insert_sql)

    def get_all(self, table_name):
        """
        Gets all items from the given table.

        :param table_name: Name of the table where data is being retrieved from.

        :return: List of dictionaries for every queried item.
        """
        
        if (table_name == "cuisine_types"):
            return [CuisineTypeModel(*param).parameters for param in self._db.select_all_query(table_name)]
        elif (table_name == "item_types"):
            return [ItemTypeModel(*param).parameters for param in self._db.select_all_query(table_name)]
        elif (table_name == "list_items"):
            return [ListItemModel(*param).parameters for param in self._db.select_all_query(table_name)]
        elif (table_name == "restaurants"):
            return [RestaurantModel(*param).parameters for param in self._db.select_all_query(table_name)]
        elif (table_name == "schedules"):
            return [ScheduleModel(*param).parameters for param in self._db.select_all_query(table_name)]
        elif (table_name == "users"):
            return [UserModel(*param).parameters for param in self._db.select_all_query(table_name)]
        else:
            raise NotImplementedError("No implementation for given table name.")

    def get_by_id(self, table_name, id):
        """
        Gets an item with the given id from the given table.

        :param table_name: Name of the table where data is being retrieved from.

        :param id: Id of the item being queried.

        :return: Dictionary containing parameters for the queried item.
        """

        try:
            items = self._db.select_all_query(table_name, {"id": id})
            if (table_name == "cuisine_types"):
                return CuisineTypeModel(*items[0]).parameters if (len(items) > 0) else None
            elif (table_name == "item_types"):
                return ItemTypeModel(*items[0]).parameters if (len(items) > 0) else None
            elif (table_name == "list_items"):
                return ListItemModel(*items[0]).parameters if (len(items) > 0) else None
            elif (table_name == "restaurants"):
                return RestaurantModel(*items[0]).parameters if (len(items) > 0) else None
            elif (table_name == "schedules"):
                return ScheduleModel(*items[0]).parameters if (len(items) > 0) else None
            elif (table_name == "users"):
                return UserModel(*items[0]).parameters if (len(items) > 0) else None
            else:
                raise NotImplementedError("No implementation for given table name.")
        # Catches error where fatchall() is attempted on None - happens when invalid table name is passed
        except AttributeError:
            raise ValueError("Given table name doesn't exist within database.")

    def insert_item(self, table_name, parameters):
        """ 
        Inserts item with given parameters into the given table within the database.

        :param table_name: Name of the table where data is being inserted into.

        :param parameters: Dictionary containing the values to be inserted into the given table.

        :return: Dictionary of parameters with database id added.
        """

        id = self._db.insert_query(table_name, parameters)
        parameters["id"] = id
        return parameters

    def update_item(self, table_name, id, parameters):
        """ 
        Updates item within given table with new parameters.

        :param table_name: Name of the table where data is being updated.

        :param id: Identifier used to determine which item to update within the database.

        :param parameters: Dictionary containing the column name->value mappings for data to be updated.

        :return: Dictionary containing parameters for the updated item after update.
        """

        self._db.update_query(table_name, parameters, {"id": id})
        return self.get_by_id(table_name, id)

    def delete_item(self, table_name, id):
        """
        Deletes item with given id from the table.

        :param table_name: Name of the table where data is being deleted.

        :param id: Identifier used to determine which item to delete within the given table.
        """

        if (self.get_by_id(table_name, id)):
            self._db.delete_query(table_name, {"id": id})
        else:
            raise Exception("Illegal deletion attempted: record with id of {} cannot be found in the database.".format(id))

    # Item List functions

    def _get_item_list(self, item_type):
        """
        Gets the list of items of the given type.

        :param item_type: Name of the item type.

        :return: List of items of the given type.
        """

        sql = "SELECT * FROM list_items WHERE item_type_id IN (SELECT id FROM item_types WHERE item_type='{}')".format(item_type)
        return self._db._read_query(sql)

    def get_states(self):
        """
        Gets the lists of states.

        :return: List of dictionaries containing data for each state.
        """

        return [ListItemModel(*param).parameters for param in self._get_item_list(STATE_ITEM_TYPE)]

    def get_weekdays(self):
        """
        Gets the lists of weekdays.

        :return: List of dictionaries containing data for each weekday.
        """

        return [ListItemModel(*param).parameters for param in self._get_item_list(WEEKDAY_ITEM_TYPE)]

    # Other functions

    def close_connection(self):
        """
        Closes the connection to the SQLite database in order to free up resources.
        """
        
        self._db.conn.close()

def reset_database_structure():
    """ Resets database values and overall structure. """
    RestaurantChooserDatabase(init_db=True).close_connection()