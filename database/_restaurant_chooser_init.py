"""
This module contains the CREATE SQL statements necessary to create the Restaurant Chooser's initial scheme.
"""

# CREATE TABLE SQL
_users_table = """
    CREATE TABLE IF NOT EXISTS users (
        id integer PRIMARY KEY,
        first_name text NOT NULL,
        middle_name text,
        last_name text NOT NULL,
        preferences_desc text,
        image_mongo_id text
    )
"""

_cuisine_types_table = """
    CREATE TABLE IF NOT EXISTS cuisine_types (
        id integer PRIMARY KEY,
        cuisine_type text NOT NULL
    )
"""

_item_types_table = """
    CREATE TABLE IF NOT EXISTS item_types (
        id integer PRIMARY KEY,
        item_type text NOT NULL
    )
"""

_list_items_table = """
    CREATE TABLE IF NOT EXISTS list_items (
        id integer PRIMARY KEY,
        item_id integer NOT NULL,
        item_name text NOT NULL,
        item_abbreviation text,
        item_type_id integer NOT NULL,
        FOREIGN KEY (item_type_id) REFERENCES item_types(id)
    )
"""

_restaurants_table = """
    CREATE TABLE IF NOT EXISTS restaurants (
        id integer PRIMARY KEY,
        name text NOT NULL,
        cuisine_type_id integer NOT NULL,
        address_line text,
        city text,
        state_id integer,
        zip text,
        phone_number text,
        suggester_id integer NOT NULL,
        FOREIGN KEY (cuisine_type_id) REFERENCES cuisine_types(id)
        FOREIGN KEY (state_id) REFERENCES list_items(item_id)
        FOREIGN KEY (suggester_id) REFERENCES users(id)
    )
"""

_schedules_table = """
    CREATE TABLE IF NOT EXISTS schedules (
        id integer PRIMARY KEY,
        restaurant_id integer NOT NULL,
        weekday_id integer NOT NULL,
        opening_time text NOT NULL,
        closing_time text NOT NULL,
        FOREIGN KEY (restaurant_id) REFERENCES restaurants(id)
        FOREIGN KEY (weekday_id) REFERENCES list_items(item_id)
    )
"""

# Tables are sorted in the order that they should be created in
CREATE_TABLES = [
    _users_table, _cuisine_types_table, _item_types_table, _list_items_table, _restaurants_table, _schedules_table
]

# Item type names (used to set up the item types table)
WEEKDAY_ITEM_TYPE = "Weekday"
STATE_ITEM_TYPE = "State"

# Initial item types SQL INSERTS
_item_types_inserts = """
    INSERT INTO item_types ( item_type )
    VALUES ( '{0}' ), ( '{1}' )
""".format(WEEKDAY_ITEM_TYPE, STATE_ITEM_TYPE)

# Initial item list SQL INSERTS for weekdays
_list_items_weekday_inserts = """
    INSERT INTO list_items ( item_id, item_name, item_abbreviation, item_type_id )
    VALUES 
        ( 1, 'Sunday', 'Sun', 1 ),
        ( 2, 'Monday', 'Mon', 1 ),
        ( 3, 'Tuesday', 'Tue', 1 ),
        ( 4, 'Wednesday', 'Wed', 1 ),
        ( 5, 'Thursday', 'Thu', 1 ),
        ( 6, 'Friday', 'Fri', 1 ),
        ( 7, 'Saturday', 'Sat', 1 )
"""

# Initial item list SQL INSERTS for states
_list_items_state_inserts = """
    INSERT INTO list_items ( item_id, item_name, item_abbreviation, item_type_id )
    VALUES
        ( 1, 'Alabama', 'AL', 2 ),
        ( 2, 'Alaska', 'AK', 2 ),
        ( 3, 'Arizona', 'AZ', 2 ),
        ( 4, 'Arkansas', 'AR', 2 ),
        ( 5, 'California', 'CA', 2 ),
        ( 6, 'Colorado', 'CO', 2 ),
        ( 7, 'Connecticut', 'CT', 2 ),
        ( 8, 'Delaware', 'DE', 2 ),
        ( 9, 'District of Columbia', 'DC', 2 ),
        ( 10, 'Florida', 'FL', 2 ),
        ( 11, 'Georgia', 'GA', 2 ),
        ( 12, 'Hawaii', 'HI', 2 ),
        ( 13, 'Idaho', 'ID', 2 ),
        ( 14, 'Illinois', 'IL', 2 ),
        ( 15, 'Indiana', 'IN', 2 ),
        ( 16, 'Iowa', 'IA', 2 ),
        ( 17, 'Kansas', 'KS', 2 ),
        ( 18, 'Kentucky', 'KY', 2 ),
        ( 19, 'Louisiana', 'LA', 2 ),
        ( 20, 'Maine', 'ME', 2 ),
        ( 21, 'Maryland', 'MD', 2 ),
        ( 22, 'Massachusetts', 'MA', 2 ),
        ( 23, 'Michigan', 'MI', 2 ),
        ( 24, 'Minnesota', 'MN', 2 ),
        ( 25, 'Mississippi', 'MS', 2 ),
        ( 26, 'Missouri', 'MO', 2 ),
        ( 27, 'Montana', 'MT', 2 ),
        ( 28, 'Nebraska', 'NE', 2 ),
        ( 29, 'Nevada', 'NV', 2 ),
        ( 30, 'New Hampshire', 'NH', 2 ),
        ( 31, 'New Jersey', 'NJ', 2 ),
        ( 32, 'New Mexico', 'NM', 2 ),
        ( 33, 'New York', 'NY', 2 ),
        ( 34, 'North Carolina', 'NC', 2 ),
        ( 35, 'North Dakota', 'ND', 2 ),
        ( 36, 'Ohio', 'OH', 2 ),
        ( 37, 'Oklahoma', 'OK', 2 ),
        ( 38, 'Oregon', 'OR', 2 ),
        ( 39, 'Pennsylvania', 'PA', 2 ),
        ( 40, 'Rhode Island', 'RI', 2 ),
        ( 41, 'South Carolina', 'SC', 2 ),
        ( 42, 'South Dakota', 'SD', 2 ),
        ( 43, 'Tennessee', 'TN', 2 ),
        ( 44, 'Texas', 'TX', 2 ),
        ( 45, 'Utah', 'UT', 2 ),
        ( 46, 'Vermont', 'VT', 2 ),
        ( 47, 'Virginia', 'VA', 2 ),
        ( 48, 'Washington', 'WA', 2 ),
        ( 49, 'West Virginia', 'WV', 2 ),
        ( 50, 'Wisconsin', 'WI', 2 ),
        ( 51, 'Wyoming', 'WY', 2 )
"""

# Initial SQL INSERTS for cuisine types
_cuisine_type_inserts ="""
    INSERT INTO cuisine_types ( id, cuisine_type )
    VALUES 
        ( 1, 'Chinese'),
        ( 2, 'Filipino'),
        ( 3, 'Italian')
"""

# These inserts should be called when the database is created for the first time
INITIAL_VALUE_INSERTS = [
    _item_types_inserts, 
    _list_items_weekday_inserts, 
    _list_items_state_inserts,
    _cuisine_type_inserts
]