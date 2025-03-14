from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/member')
def member():
    with open("templates/heros.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    return render_template('heros.html', members=news_list["stuff"])


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
