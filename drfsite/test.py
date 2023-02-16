import requests

url = "http://127.0.0.1:8000/api/v1/womenlist/"
head = {'title': 'Parampa', 'content': 'fdfkdfk lavina', 'cat':1}
k = requests.post(url, data=head)
print(k.json())