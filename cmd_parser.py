"""
This module contains code that defines the possible command line arguments and parses them accordingly.
"""

# Built-in module
from sys import argv

# Argument constants
_prod = "--prod"
_reset_db = "--reset-db"

# Command line argument dictionary
_kwds = {
    _prod : False,
    _reset_db : False
}

# Shortcuts dictionary
_kwd_shortcuts = {
    "-p" : _prod,
    "-r" : _reset_db
}

# Parses the passed command line arguments accordingly (if any)
for arg in argv[1:]:
    # Checks for keyword shortcuts then validates associated argument
    if arg in _kwd_shortcuts:
        full_arg = _kwd_shortcuts[arg]
        _kwds[full_arg] = True
    # Checks for the full argument
    elif arg in _kwds:
        _kwds[arg] = True

# Argument boolean flags
ARG_PROD_FLAG = _kwds[_prod]
ARG_RESET_DB_FLAG = _kwds[_reset_db]
