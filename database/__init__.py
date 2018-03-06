"""
This module is responsible for performing SQLite database operations. It is written generically, so that 
other modules can use it as a wrapper for their own specialized database operations.
"""

# Built-in modules
from os.path import join
import sqlite3
from sqlite3 import Error

# User-defined modules
from config import DATA_DIR, DB_NAME
from utilities import get_base_path

class DatabaseAccessor(object):
    """
    Class responsible for accessing the SQLite database containing the application data.
    """
    
    def __init__(self):
        self.database_path = join(get_base_path(), DATA_DIR, DB_NAME)
        
    def create_connection(self):
        """ 
        Creates a database connection to a SQLite database.
        """
        try:
            self.conn = sqlite3.connect(self.database_path)
        except Error as e:
            print(e)
        
    def execute(self, sql, parameters=None):
        """ 
        Executes given SQL statement. Other functions may serve as wrappers of this function
        in order to carry out more specific tasks.
        
        :param sql: A SQL statement.
        
        :param parameters: Parameters to be injected into the SQL statement, if any.

        :return: Resulting cursor object from executing the query.
        """

        try:
            c = self.conn.cursor()
            if parameters:
                c.execute(sql, parameters)
            else:
                c.execute(sql)
            return c
        except Error as e:
            print(e)
            
    def _read_query(self, sql, parameters=None):
        """ 
        Generic function that reads data from database using given SQL statement.

        :param sql: A read SQL statement.

        :param parameters: Parameters to be injected into the SQL statement, if any.

        :return: Data results of the given SQL statement.
        """

        cursor = self.execute(sql, parameters)
        return cursor.fetchall()

    def _write_query(self, sql, parameters=None):
        """
        Generic function that writes data to database using given SQL statement.

        :param sql: A write SQL statement.

        :param parameters: Parameters to be injected into the SQL statement, if any.

        :return: ID of the newly created item, if any.
        """

        cursor = self.execute(sql, parameters)
        self.conn.commit()
        return cursor.lastrowid if cursor else None

    @classmethod
    def _parse_where_conditions(cls, where_parameters):
        """
        Transforms the passed parameters into a WHERE clause.

        :param where_parameters: Dictionary mapping column_names to their associated values 
        in order to determine the contents of the WHERE clause.

        :return: WHERE clause with the parameters inserted.
        """

        if not where_parameters:
            return ""
        else:
            where_clause = ""
            for column_name in where_parameters:
                if len(where_clause) == 0:
                    where_clause = "WHERE " + column_name + "=:" + column_name
                else:
                    where_clause += ", " + column_name + "=:" + column_name
            return where_clause

    def select_all_query(self, select_table, where_parameters=None):
        """
        Performs read from given table for all records (plus a WHERE clause filter).

        :param select_table: Target table being read.

        :param where_parameters: Dictionary mapping column_names to their associated values 
        in order to determine the contents of the WHERE clause.

        :return: Data results of the given SQL statement.
        """

        # Set WHERE SQL statement
        where_statement = DatabaseAccessor._parse_where_conditions(where_parameters)

        # Set rest of SQL query
        sql = "SELECT * FROM {0} {1}".format(select_table, where_statement)
        return self._read_query(sql, where_parameters)

    def insert_query(self, insert_table, parameters):
        """
        Performs insert into given table using given parameters.

        :param insert_table: Target table where insertion is to be performed.

        :param parameters: Dictionary of arguments were key = column name and value = set value.

        :return: ID of newly inserted item.
        """

        # Sets up the column names and parameterized values for SQL query
        columns = []
        values = []
        for column_name in parameters:
            columns.append(column_name)
            values.append(':' + column_name)

        # Executes INSERT accordingly
        sql = "INSERT INTO {0} ({1}) VALUES ({2})".format(insert_table, ",".join(columns), ",".join(values))
        return self._write_query(sql, parameters)

    def update_query(self, update_table, parameters, where_parameters=None):
        """
        Performs update within given table using given parameters.

        :param update_table: Target table where update is to be performed.

        :param parameters: Dictionary of arguments were key = column name and value = set value.

        :param where_parameters: Dictionary mapping column_names to their associated values 
        in order to determine the contents of the WHERE clause.
        """

        # Set SET SQL statement
        set_statement = ""
        for column_name in parameters:
            if len(set_statement) == 0:
                set_statement = column_name + "=:" + column_name
            else:
                set_statement += ", " + column_name + "=:" + column_name

        # Set WHERE SQL statement
        where_statement = DatabaseAccessor._parse_where_conditions(where_parameters)

        # Add WHERE parameters to the original dictionary of parameters
        for column_name, value in where_parameters.items():
            parameters[column_name] = value

        # Executes update accordingly
        sql = "UPDATE {0} SET {1} {2}".format(update_table, set_statement, where_statement)
        self._write_query(sql, parameters)

    def delete_query(self, delete_table, where_parameters=None):
        """
        Performs delete within given table using given WHERE clause to select the items targeted for deletion.

        :param delete_table: Target table where delete is to be performed.

        :param where_parameters: Dictionary mapping column_names to their associated values 
        in order to determine the contents of the WHERE clause.
        """

        # Set WHERE SQL statement
        where_statement = DatabaseAccessor._parse_where_conditions(where_parameters)

        # Executes delete accordingly
        sql = "DELETE FROM {0} {1}".format(delete_table, where_statement)
        self._write_query(sql, where_parameters)
        
    def close_connection(self):
        """
        Closes the connection to the SQLite database in order to free up resources.
        """
        self.conn.close()