from data import db_session
from data.departments import Department
from data.users import User
from data.jobs import Job
from data.departments import Department

import sqlalchemy
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

db_session.global_init('db/users.sqlite')
db_sess = db_session.create_session()

user = db_sess.query(User).filter(User.id == 1).first()
dep = Department(title='Медицинский раздел', chief=2, members=[1, 2], email='medicine@mars.org')
user.dep.append(dep)
db_sess.commit()

qe = db_sess.query(User).select_from(User).join(Job, User.id == Job.team_leader,
                                                isouter=True).filter(Job.work_size > 25, Department.id == 1)
for i in qe:
    print(i.surname, i.name)
