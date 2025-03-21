from flask import Flask, render_template, request

app = Flask(__name__)

cnt_pic = 3


@app.route('/carousel', methods=['POST', 'GET'])
def carousel():
    global cnt_pic
    if request.method == 'GET':
        return render_template('hehe.html')
    elif request.method == 'POST':
        file = request.files['file']
        cnt_pic += 1
        file.save(f'static/img/{cnt_pic}.png')
        return render_template('hehe.html', new=f'static/img/{cnt_pic}.png')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
