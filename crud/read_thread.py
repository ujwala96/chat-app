from database.db_connector import *


# This should only return available threads
def get_threads(database):

    connection = connect_to_db(database_name=database)
    cursor = connection.cursor()

    select_query = """select * from threads"""
    threads_info = cursor.execute(select_query)

    threads_dict = {}
    for id, each_thread in enumerate(threads_info):
        threads_dict[id] = list(each_thread)

    connection.close()

    return threads_dict


def get_thread_messages(thread_id, database):
    connection = connect_to_db(database_name=database)
    cursor = connection.cursor()

    select_message_query = f"""select * from messages where thread_id='{thread_id}' order by create_at asc"""
    cursor.execute(select_message_query)
    messages_data = cursor.fetchall()
    connection.close()
    return messages_data
