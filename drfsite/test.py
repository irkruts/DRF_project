import requests

url = "http://127.0.0.1:8000/api/v1/womenlist/"
head = {'title': 'Irina', 'content': 'Irina Kruts', 'cat_id':2}
k = requests.post(url, data=head)
print(k.json())