import os.path
from database.db_connector import connect_to_db
from database.create_table import create_tables
from crud.create_thread import create_thread
from crud.read_thread import get_threads, get_thread_messages
from crud.update_thread import update_thread
from crud.delete_thread import delete_thread


def check_database_exists(database_name):
    return os.path.exists(database_name)


database_name = "chat.db"

if check_database_exists(database_name):
    print("Database exists.")
else:
    connect_to_db(database_name=database_name)
    create_tables(database_name)

options = {
    0: "Start new thread",
    1: "Read threads",
    2: "Continue with existing thread",
    3: "Delete existing thread",
}


def main():
    print("select Options: ")
    for key, value in options.items():
        print(f"{key} : {value}")

    choice = int(input("Enter option index:"))
    initial_message = True

    while True:
        if choice == 0:
            while True:
                if initial_message:
                    msg_val = input("Enter Msg: ")
                    thread_id, response = create_thread(
                        msg=msg_val, database=database_name
                    )
                    print(response)
                    initial_message = False
                else:
                    msg_val = input("Enter Msg: ")
                    response = update_thread(
                        thread_id, database=database_name, message=msg_val
                    )
                    print(response)
        elif choice == 1:
            print("select thread id: ")
            threads_dict = get_threads(database=database_name)
            for each_thread in threads_dict:
                print(f"{each_thread}: {threads_dict[each_thread][1]}")

            thread_index = int(input("Enter message thread index:"))
            thread_id = threads_dict[thread_index][0]
            messages = get_thread_messages(thread_id, database=database_name)
            print(messages)

        elif choice == 2:
            threads_dict = get_threads(database=database_name)
            for each_thread in threads_dict:
                print(f"{each_thread}: {threads_dict[each_thread][1]}")

            thread_index = int(input("Enter message thread index:"))
            thread_id = threads_dict[thread_index][0]
            messages_data = get_thread_messages(thread_id, database=database_name)
            history = []
            for each_message in messages_data:
                history.append({"role": each_message[1], "content": each_message[2]})
            while True:
                msg_val = input("Enter msg: ")
                response = update_thread(
                    thread_id, database=database_name, message=msg_val, history=history
                )
                print(response)
        elif choice == 3:
            threads_dict = get_threads(database=database_name)
            for each_thread in threads_dict:
                print(f"{each_thread}: {threads_dict[each_thread][1]}")

            thread_index = int(input("Enter message thread index for delete:"))
            thread_id = threads_dict[thread_index][0]
            delete_thread(thread_id, database=database_name)


if __name__ == "__main__":
    main()
