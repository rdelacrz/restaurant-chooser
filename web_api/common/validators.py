"""
This module contains multiple validators for use by the api.
"""

# Built-in modules
import re

_phone_pattern = re.compile(r"^(?:\d-)?\d{3}-\d{3}-\d{4}$")
def phone_number(phone_str):
    """
    Validates a given string to determine that it is truly a phone number.
    
    :param phone_str: String containing the phone number to be validated.

    :return: Returns the original string if it is a valid phone number, raises an exception in other cases.
    """
    
    if (_phone_pattern.match(phone_str)):
        return phone_str
    else:
        raise ValueError('{} is not a valid phone number'.format(phone_str))

_zip_pattern = re.compile(r"^\d{5}(?:-\d{4})?$")
def zip_code(zip_str):
    """
    Validates a given string to determine that it is truly a zip code.
    
    :param zip_str: String containing the zip code to be validated.

    :return: Returns the original string if it is a valid zip code, raises an exception in other cases.
    """

    if (_zip_pattern.match(zip_str)):
        return zip_str
    else:
        raise ValueError('{} is not a valid zip code'.format(zip_str))

_time_pattern = re.compile(r"^(?:0[0-9]|1[0-2]):[0-5][0-9] (?:A|P)M$")
def time(time_str):
    """
    Validates a given string to determine that it is truly a time string.

    :param time_str: String containing the time string to be validated.

    :return: Returns the original string if it is a valid time string, raises an exception in other cases.
    """

    if (_time_pattern.match(time_str)):
        return time_str
    else:
        raise ValueError('{} is not a valid time'.format(time_str))