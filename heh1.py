from flask import Flask, render_template

app = Flask(__name__)


@app.route('/list_prof/<sign>')
def training(sign):
    return render_template('training.html', sign=sign)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
