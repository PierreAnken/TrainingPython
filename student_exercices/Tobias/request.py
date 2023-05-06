import requests

response = requests.get('http://preplounge.de')

# for key, value in response.__dict__.items():
#     print(key, ':', value)


index_dream = response.text.index('dream')
print(response.text[index_dream-20:index_dream],response.text[index_dream+5:index_dream+20+5])
