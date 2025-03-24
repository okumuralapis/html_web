from data.departments import Department

name = input()
global_init(name)
db_sess = create_session()

qe1 = db_sess.query(Department).filter(Department.id == 1).first()
dep = sorted(set(list(map(int, qe1.members.split(', '))) + [qe1.chief]))
re = []
for user, job in db_sess.query(User, Jobs).join(Jobs).filter(User.id.in_(dep)):
    hours = job.work_size if job.work_size else 0
    for jb in db_sess.query(Jobs).filter(Jobs.collaborators.like(f'%{user.id}%')):
        hours += jb.work_size
    if hours > 25:
        if (user.surname, user.name) not in re:
            print(user.surname, user.name)
            re.append((user.surname, user.name))
