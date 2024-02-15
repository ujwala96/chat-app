# Chat Application

This is a simple command-line chat application that allows users to interact with threads and messages. Users can perform various operations such as starting a new thread, reading existing threads, continuing with existing threads, and deleting threads. The application uses a SQLite database to store thread and message data.

## Requirements

- Python 3.10
- SQLite3

## Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    ```

2. Navigate to the project directory:

    ```bash
    cd <project-directory>
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Ensure that the `chat.db` file exists in the project directory. If not, it will be created automatically upon running the application.

2. Create a .env file and add your Openai API key

    ```bash
    OPENAI_API_KEY=<your_openai_api_key>
    ```

2. Run the application:

    ```bash
    python chat_app.py
    ```

3. Select one of the available options:
    - **Start new thread** (Option 0): Start a new conversation thread.
    - **Read threads** (Option 1): View existing threads and their messages.
    - **Continue with existing thread** (Option 2): Add a new message to an existing thread.
    - **Delete existing thread** (Option 3): Delete an existing thread and its messages.

4. Follow the prompts to interact with the application based on the selected option.

## Functionality

- **Start new thread**: Allows users to start a new conversation thread by entering a message.
- **Read threads**: Displays existing threads along with their messages.
- **Continue with existing thread**: Enables users to add new messages to an existing thread.
- **Delete existing thread**: Allows users to delete an existing thread and all its messages.

## Contributors

- [Ujwala Brahmarouthu]

## License

This project is licensed under the [MIT License](LICENSE).
