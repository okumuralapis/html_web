from data import db_session
from data.users import User
from data.jobs import Job
from data.departments import Department
import sqlalchemy
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

db_session.global_init('db/users.sqlite')
db_sess = db_session.create_session()

check = []
qe1 = db_sess.query(Department).filter(Department.id == 1).first()
dep = list(map(int, qe1.members.split(', ')))
for user, job in db_sess.query(User).filter(User.id.in_(dep)):
    hours = 0
    for jb in db_sess.query(Jobs).all():
        col = list(map(int, jb.collaborators.split(', ')))
        if user.id in col:
            hours += jb.work_size
    if hours > 25 and (user.surname, user.name) not in check:
        print(user.surname, user.name)
        check.append((user.surname, user.name))
