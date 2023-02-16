import requests

url = "http://127.0.0.1:8000/api/v1/women/"
head = {'title': 'NEWJOL', 'content': 'fdfkdfk lavina', 'cat':1}
k = requests.delete(url, data=head)
print(k.json())