from flask import Flask, render_template

app = Flask(__name__)

d = {
    'title': 'Анкета',
    'surname': 'Watny',
    'name': 'Mark',
    'education': 'выше среднего',
    'profession': 'штурман марсохода',
    'sex': 'male',
    'motivation': 'Всегда мечтал застрять на Марсе!',
    'ready': True}

@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=d["title"])

@app.route('/answer')
@app.route('/auto_answer')
def ans():
    return render_template('auto_answer.html', info=d)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
