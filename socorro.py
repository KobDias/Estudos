import os
from mistralai import Mistral
from dotenv import load_dotenv
from getpass import getpass
import numpy as np

load_dotenv()
MISTRAL_API_KEY = os.getenv('MISTRAL_API_KEY')

api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-large-latest" # acesso ao chat

client = Mistral(api_key=api_key)

text= getpass("")

chat_response = client.chat.complete(
    model= model,
    messages = [
        {
            "role": "user",
            "content": {text},
            "type": "text"
        },
    ]
)
print(chat_response.choices[0].message.content)

