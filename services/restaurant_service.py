"""
This module contains the service used to perform restaurant-related operations. All functions defined here
will override the functions defined in the base service.
"""


# User-defined modules
from services import BaseService
from models import ScheduleModel
from view_models import FullRestaurantDataModel

class RestaurantService(BaseService):
    """
    Service specialized for restaurabt operations.
    """

    def __init__(self):
        super().__init__("restaurants")

    def insert_item(self, db_obj, parameters):
        """ 
        Inserts restaurant with given parameters into the SQLite database, alongside any associated schedule data
        passed.

        :param db_obj: SQLite database object being used to get the data.

        :param parameters: Dictionary containing the values to be inserted into the database.

        :return: Dictionary of parameters with database id added.
        """
        
        # Parses parameter data
        restaurant_dict = FullRestaurantDataModel(**parameters).parameters
        schedule_dict_list = [ScheduleModel(**schedule).parameters for schedule in restaurant_dict.pop("schedule_items")]

        # Inserts restaurant first (with empty schedule list)
        restaurant_data = FullRestaurantDataModel(**db_obj.insert_item(self.table_name, restaurant_dict))
        restaurant_data.schedule_times = []

        # Then inserts schedules into restaurant data
        for schedule_dict in schedule_dict_list:
            restaurant_data.schedule_times.append(ScheduleModel(**db_obj.insert_item("schedules", schedule_dict)))

        return restaurant_data
