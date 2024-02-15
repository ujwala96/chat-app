from database.db_connector import *


def query_execution(conn, query):
    try:
        c = conn.cursor()
        c.execute(query)
    except Error as e:
        print(e)


def create_tables(database_name):

    create_query_threads = """CREATE TABLE IF NOT EXISTS threads (
                    thread_id CHAR PRIMARY KEY,
                    First_message TEXT
                )"""

    create_query_messages = """CREATE TABLE IF NOT EXISTS messages (
                    thread_id INTEGER ,
                    role CHAR,
                    content TEXT,
                    create_at TIMESTAMP,
                    FOREIGN KEY (thread_id) REFERENCES threads(thread_id)
                )"""

    conn = connect_to_db(database_name)

    if conn is not None:
        query_execution(conn, create_query_threads)
        query_execution(conn, create_query_messages)
    else:
        print("Error! cannot create the database connection.")


if __name__ == "__main__":
    create_tables(database=None)
