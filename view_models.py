"""
This module contains all the view models that are used to encapsulate data passed from the frontend that do not
correspond with regular models associated with the database tables.
"""

# User-defined models
from models import _ParentModel

class FullUserDataModel(_ParentModel):
    """ Model for user data and its associated image file data. """

    def __init__(self, id=None, first_name=None, middle_name=None, last_name=None, preferences_desc=None, file_data=None):
        self.id = id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.preferences_desc = preferences_desc
        self.file_data = file_data

class FileDataModel(_ParentModel):
    """ Model for file data pulled from a HTML file input. """

    def __init__(self, file_name=None, file_type=None, base_64_data=None):
        self.file_name = file_name
        self.file_type = file_type
        self.base_64_data = base_64_data

class FullRestaurantDataModel(_ParentModel):
    """ Model for restaraunt data along with associated schedule data. """

    def __init__(self, id=None, name=None, cuisine_type_id=None, address_line=None, city=None, state_id=None, 
            zip=None, phone_number=None, suggester_id=None, schedule_times=None):
        self.id = id
        self.name = name
        self.cuisine_type_id = cuisine_type_id
        self.address_line = address_line
        self.city = city
        self.state_id = state_id
        self.zip = zip
        self.phone_number = phone_number
        self.suggester_id = suggester_id
        self.schedule_times = schedule_times