from database.db_connector import *


def delete_thread(thread_id, database):

    connection = connect_to_db(database_name=database)
    cursor = connection.cursor()

    delete_thread_query = f"""DELETE FROM threads where thread_id='{thread_id}'"""
    delete_thread_message_query = (
        f"""DELETE FROM messages where thread_id='{thread_id}'"""
    )
    cursor.execute(delete_thread_query)
    cursor.execute(delete_thread_message_query)

    connection.commit()
    connection.close()
