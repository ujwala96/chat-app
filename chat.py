from openai import OpenAI
import os
from config import openai_api_key

os.environ["OPENAI_API_KEY"] = openai_api_key
client = OpenAI()


class MSG:
    def __init__(self, history) -> None:
        self.model = "gpt-3.5-turbo"
        self.history = history
        self.thread = []

    def call(self, msg) -> str:
        user_msg = {"role": "user", "content": msg}
        self.history.append(user_msg)

        completion = client.chat.completions.create(
            model=self.model, messages=self.history
        )
        assistant_msg = {
            "role": "assistant",
            "content": completion.choices[0].message.content,
        }
        self.history.append(assistant_msg)
        return completion.choices[0].message.content, self.history
