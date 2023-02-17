import requests

url = "http://127.0.0.1:8000/api/v1/women/category"
head = {'title': 'NEWJOL', 'content': 'fdfkdfk lavina', 'cat':1}
k = requests.get(url)
print(k.json())