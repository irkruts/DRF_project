import requests
from fake_useragent import UserAgent

ua = UserAgent()
url = "http://127.0.0.1:8000/api/v1/auth/users/"
url2 = "http://127.0.0.1:8000/auth/token/login/" #{'auth_token': '3941cc03987b5530781d38b7fde1996fb4109dce'}

head = {'username': 'seconduser',
        'password': 'ser12345',
        }
        # 'email': 'seconduser@gmail.com'}
k = requests.post(url2, data=head)
# print(k.json())

# url3 = "http://127.0.0.1:8000/api/v1/women/1/"
# token = '3941cc03987b5530781d38b7fde1996fb4109dce'
# header = {
#     'User-Agent': ua.random,
#     "Authorization": f"Token {token}"
# }
# new = requests.get(url3, headers=header)
# print(new.json())


url2 = "http://127.0.0.1:8000/auth/token/login/"