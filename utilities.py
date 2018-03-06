"""
General purpose functions for the application to utilize.
"""

# Built-in modules
import os

# User-defined modules
from config import DATA_DIR

def get_base_path():
    """
    Gets the base path for the application directory. The current file must be in the base
    directory for this function to work as intended.

    :return: Base path for the application directory.
    """
    return os.path.dirname(os.path.abspath(__file__))

def clear_data(base_dir=DATA_DIR):
    """
    Recursively clears all files within the given directory (the root directory is app data directory 
    by default).

    :param base_dir: Base directory to begin the process of file deletion.
    """

    for item in os.listdir(base_dir):
        path = os.path.join(base_dir, item)

        # This line exists as a safeguard to prevent file deletions in a directory outside of the app data directory
        if (DATA_DIR not in path):
            raise Exception("Illegal operation attempted: deletion attempted in a directory outside of the app data directory.")
            
        # Deletes file or recursively clears data within the traversed directory
        if os.path.isfile(path):
            os.remove(path)
        else:
            clear_data(path)