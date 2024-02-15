from database.db_connector import *
from datetime import datetime
from chat import MSG


def update_thread(thread_id, database, message, history):
    msg_app = MSG(history=history)
    connection = connect_to_db(database_name=database)
    cursor = connection.cursor()
    current_datetime = datetime.now().isoformat()

    message_insert_query = """INSERT INTO messages VALUES(?, ?, ?, ?)"""
    cursor.execute(message_insert_query, [thread_id, "user", message, current_datetime])

    response, history = msg_app.call(message)
    cursor.execute(
        message_insert_query, [thread_id, "assistant", response, current_datetime]
    )

    connection.commit()
    connection.close()
    return response
