import uuid
from datetime import datetime
from database.db_connector import *
from chat import MSG


def create_thread(msg, database):
    msg_app = MSG(
        history=[{"role": "system", "content": "You are a helpful assistant."}]
    )
    current_datetime = datetime.now().isoformat()
    connection = connect_to_db(database_name=database)
    cursor = connection.cursor()
    thread_id = str(uuid.uuid4())

    message_insert_query = """INSERT INTO messages VALUES(?, ?, ?, ?)"""
    thread_insert_query = """ INSERT INTO threads VALUES(?, ?)"""

    values = [thread_id, msg]
    cursor.execute(thread_insert_query, values)

    cursor.execute(message_insert_query, [thread_id, "user", msg, current_datetime])

    response, history = msg_app.call(msg)
    cursor.execute(
        message_insert_query, [thread_id, "assistant", response, current_datetime]
    )

    connection.commit()
    connection.close()

    return thread_id, response
