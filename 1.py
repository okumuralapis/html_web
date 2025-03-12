from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/distribution')
def distr():
    return render_template('distribution.html', names=['Ридли Скотт', 'Энди Уир', 'Марк Уортни',
                                                      'Венката Капур', 'Тедди Санднерс', 'Шон Бин'])


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
