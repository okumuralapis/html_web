from data import db_session
from data.users import User
from data.jobs import Job
import sqlalchemy
from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init('db/users.sqlite')
    app.run()


@app.route("/")
def index():
    db_sess = db_session.create_session()
    info = db_sess.query(Job, User).join(User).all()
    return render_template('index.html', info=info)


if __name__ == '__main__':
    main()
