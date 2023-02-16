import requests

url = "http://127.0.0.1:8000/api/v1/womenlist/50/"
head = {'title': 'JULIA', 'content': 'lavina', 'cat_id':2}
k = requests.put(url, data=head)
print(k.json())