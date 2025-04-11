from requests import post, get, delete

print(get('http://localhost:5000/api/v2/users').json())  # получение всех модулей

# тестирование get
print(get('http://localhost:5000/api/v2/users/1').json())  # верный первый пользователь
print(get('http://localhost:5000/api/v2/users/hehe').json())  # неверный/строка
print(get('http://localhost:5000/api/v2/users/123').json())  # неверный/нет пользователя

# тестирование post
print(post('http://localhost:5000/api/v2/users', json={}).json())
print(post('http://localhost:5000/api/v2/users',
           json={'name': 'hehehe'}).json())
print(post('http://localhost:5000/api/v2/users',
           json={'surname': 'Heh',
                 'name': 'Hih',
                 'speciality': 'friend of a clown',
                 'position': 'clown',
                 'email': 'hihihaha@mail.ru',
                 'password': 'hihihaha67'}).json())

# тестирование delete
print(delete('http://localhost:5000/api/v2/users/1').json())  # верный первый пользователь
print(delete('http://localhost:5000/api/v2/users/hehe').json())  # неверный/строка
print(delete('http://localhost:5000/api/v2/users/123').json())  # неверный/нет пользователя

print(get('http://localhost:5000/api/v2/users').json())
