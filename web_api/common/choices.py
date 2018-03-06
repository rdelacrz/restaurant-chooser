"""
This module contains methods that query specific values from the database in order to produce the 
range of choices that certain arguments will use.
"""

# User-defined modules
from database.restaurant_chooser_database import RestaurantChooserDatabase

def _get_weekday_ids():
    """
    Gets the list of ids associated with the weekdays stored in the database.

    :return: List of integer ids associated with the available weekdays.
    """

    temp_db = RestaurantChooserDatabase()
    weekday_list = [weekday_obj["item_id"] for weekday_obj in temp_db.get_weekdays()]
    temp_db.close_connection()
    return weekday_list

def _get_state_ids():
    """
    Gets the list of ids associated with the states stored in the database.

    :return: List of integer ids associated with the available states.
    """

    temp_db = RestaurantChooserDatabase()
    state_list = [weekday_obj["item_id"] for weekday_obj in temp_db.get_states()]
    temp_db.close_connection()
    return state_list

weekday_ids = _get_weekday_ids()
state_ids = _get_state_ids()