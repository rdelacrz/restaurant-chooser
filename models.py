"""
Module containing all the Python models that will be used to represent entities from the SQL database tables.
"""

class _ParentModel(object):
    """ Parent class for all models. """

    @property
    def parameters(self):
        """ Gets the column name->value mappings of each model. """
        return self.__dict__

class CuisineTypeModel(_ParentModel):
    """ Model for cuisine types. """

    def __init__(self, id=None, cuisine_type=None):
        self.id = id
        self.cuisine_type = cuisine_type

class ItemTypeModel(_ParentModel):
    """ Model for item types. """

    def __init__(self, id=None, item_type=None):
        self.id = id
        self.item_type = item_type

class ListItemModel(_ParentModel):
    """ Model for list items. """

    def __init__(self, id=None, item_id=None, item_name=None, item_abbreviation=None, item_type=None):
        self.id = id
        self.item_id = item_id
        self.item_name = item_name
        self.item_abbreviation = item_abbreviation
        self.item_type = item_type

class RestaurantModel(_ParentModel):
    """ Model for restaurants. """

    def __init__(self, id=None, name=None, cuisine_type_id=None, address_line=None, city=None, state_id=None, 
            zip=None, phone_number=None, suggester_id=None):
        self.id = id
        self.name = name
        self.cuisine_type_id = cuisine_type_id
        self.address_line = address_line
        self.city = city
        self.state_id = state_id
        self.zip = zip
        self.phone_number = phone_number
        self.suggester_id = suggester_id

class ScheduleModel(_ParentModel):
    """ Model for schedules. """

    def __init__(self, id=None, restaurant_id=None, weekday_id=None, opening_time=None, closing_time=None):
        self.id = id
        self.restaurant_id = restaurant_id
        self.weekday_id = weekday_id
        self.opening_time = opening_time
        self.closing_time = closing_time

class UserModel(_ParentModel):
    """ Model for users. """

    def __init__(self, id=None, first_name=None, middle_name=None, last_name=None, preferences_desc=None, image_mongo_id=None):
        self.id = id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.preferences_desc = preferences_desc
        self.image_mongo_id = image_mongo_id