
import requests

response = requests.get('https://type.fit/api/quotes')
data = response.json()

print(type(data), type(data[0]))
print(data[0])

