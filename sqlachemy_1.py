from data import db_session
from data.users import User
from data.jobs import Job
import sqlalchemy

db_session.global_init("db/users.db")
db_sess_user = db_session.create_session()

user = User()
user.surname = 'Scott'
user.name = 'Ridley'
user.position = 'captain'
user.speciality = 'research engineer'
user.address = 'module_1'
user.email = 'scott_chief@mars.org'
db_sess_user.add(user)
db_sess_user.commit()

db_session.global_init("db/jobs.db")
db_sess = db_session.create_session()

job = Job()
job.team_leader = 1
job.job = 'deployment of residential modules 1 and 2'
job.work_size = 15
job.collaborators = '2, 3'
job.start_date = '(now)'
job.is_finished = False
db_sess.add(job)
db_sess.commit()
