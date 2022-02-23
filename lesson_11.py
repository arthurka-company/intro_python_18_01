# requests

import requests

# requests.get()
# requests.post()
# requests.patch()
# requests.put()
# requests.delete()
#
# response = requests.get('https://jsonplaceholder.typicode.com/')
#
# if response.status_code == 200:
#     print('Ok')
#     print(response.status_code)
#     print(response.content)
#     print(response.text)
#     print(response.json())
# else:
#     print('Error')


# response = requests.get('https://jsonplaceholder.typicode.com/posts/')
# response = requests.get('https://jsonplaceholder.typicode.com/posts/5')
# response = requests.get('https://jsonplaceholder.typicode.com/posts/?userId=1')
# response = requests.get(
#     'https://jsonplaceholder.typicode.com/posts/',
#     params={'userId': 1},
#     headers={
#         'Authorization': 'Token ifuhqih3hwo37ghw3o4th384ho4ht'
#     }
# )
#
# if response.status_code == 200:
#     print('Ok')
#     print(response.status_code)
#     print(response.json())
# else:
#     print('Error')



# response = requests.post(
#     'https://jsonplaceholder.typicode.com/posts/',
#     data={'title': 'Test title', 'body': 'Test ok reddfdf', 'userId': 10000}
# )
# print(response.status_code)
# print(response.json())

element = requests.get('https://jsonplaceholder.typicode.com/posts/1')
print(element.json())
# response = requests.patch(
#     'https://jsonplaceholder.typicode.com/posts/1',
#     data={'title': 'Test title'}
# )
# print(response.status_code)
# print(response.json())


response = requests.put(
    'https://jsonplaceholder.typicode.com/posts/1',
    data={'title': 'Test title'}
)
print(response.status_code)
print(response.json())

# beautifulsoup - парсинга html
