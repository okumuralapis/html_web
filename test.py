from requests import post, get, delete

print(get('http://localhost:5000/api/v2/jobs').json())  # получение всех работ

# тестирование get
print(get('http://localhost:5000/api/v2/jobs/1').json())  # верная работа
print(get('http://localhost:5000/api/v2/jobs/hehe').json())  # неверный/строка
print(get('http://localhost:5000/api/v2/jobs/123').json())  # неверный/не существующий ид

# тестирование post
print(post('http://localhost:5000/api/v2/jobs', json={}).json())
print(post('http://localhost:5000/api/v2/jobs',
           json={'title': 'hehehe'}).json())
print(post('http://localhost:5000/api/v2/jobs',
           json={'team_leader': 1,
                 'job': 'Clowning',
                 'work_size': 30,
                 'collaborators': '1 2 3',
                 'is_finished': True,
                 'category': 2}).json())

# тестирование delete
print(delete('http://localhost:5000/api/v2/jobs/1').json())  # верная работа
print(delete('http://localhost:5000/api/v2/jobs/hehe').json())  # неверный/строка
print(delete('http://localhost:5000/api/v2/jobs/123').json())  # неверный/не существующий ид

print(get('http://localhost:5000/api/v2/jobs').json())
