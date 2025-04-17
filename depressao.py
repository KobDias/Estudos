from mistralai import Mistral
import requests
import numpy as np
import faiss
import os
from getpass import getpass

api_key= getpass("Type your API Key")
client = Mistral(api_key=api_key)

response = requests.get('https://raw.githubusercontent.com/run-llama/llama_index/main/docs/docs/examples/data/paul_graham/paul_graham_essay.txt')
text = response.text

f = open('essay.txt', 'w')
f.write(text)
f.close()

chunk_size = 2048
chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
print(len(chunks))
