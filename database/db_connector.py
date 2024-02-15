import sqlite3
from sqlite3 import Error


def connect_to_db(database_name):
    connection = None
    try:
        connection = sqlite3.connect(database_name)
        return connection
    except Error as e:
        print(e)
