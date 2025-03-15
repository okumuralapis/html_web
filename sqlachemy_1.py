from data import db_session
from data.users import User
from data.jobs import Job
import sqlalchemy
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init('db/users.sqlite')

    user = User()
    user.surname = 'Scott'
    user.name = 'Ridley'
    user.position = 'captain'
    user.speciality = 'research engineer'
    user.address = 'module_1'
    user.email = 'scott_chief@mars.org'
    db_sess_user = db_session.create_session()
    db_sess_user.add(user)
    db_sess_user.commit()

    user = db_sess_user.query(User).filter(User.id == 1).first()
    job = Job(team_leader=1, job='development of residential modules 1 and 2',
              work_size=15, collaborators='2, 3', start_date='(now)',
              is_finished=False)
    user.job.append(job)
    db_sess_user.commit()


if __name__ == '__main__':
    main()
