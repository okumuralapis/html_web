from data import db_session
from data.users import User
from data.jobs import Job
from forms.user import RegisterForm_user, LoginForm_user
from forms.job import RegisterForm_job
import sqlalchemy
from flask import Flask, render_template, redirect, abort, request
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


def main():
    db_session.global_init('db/users.db')
    app.run()


@app.route("/")
def index():
    db_sess = db_session.create_session()
    info = db_sess.query(Job, User).join(User).all()
    return render_template('index.html', info=info)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm_user()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            surname=form.surname.data,
            name=form.name.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data,
            email=form.email.data)
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm_user()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/jobs', methods=['GET', 'POST'])
def reqister_job():
    form = RegisterForm_job()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        if db_sess.query(Job).filter(Job.job == form.job.data).first():
            return render_template('reg_job.html', title='Регистрация',
                                   form=form,
                                   message="Такая работа уже есть")
        job = Job()
        job.team_leader = form.team_leader.data
        job.job = form.job.data
        job.work_size = form.work_size.data
        job.collaborators = form.collaborators.data
        job.is_finished = form.is_finished.data
        return redirect('/')
    return render_template('reg_job.html', title='Добавление работы', form=form)


if __name__ == '__main__':
    main()
