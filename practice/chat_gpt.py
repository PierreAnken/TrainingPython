import os

import openai

openai.api_key = os.environ['GPT_KEY']

response = openai.Image.create(
  prompt="Fondue fromage, à Noël",
  n=5,
  size="1024x1024"
)
print(response['data'])
