from flask import Flask, render_template
import time

app = Flask(__name__)


@app.route('/bobo')
def index_bobo():
    time.sleep(2)
    return render_template('index.html', name='bobo')


@app.route('/gmwang')
def index_gmwang():
    time.sleep(2)
    return render_template('index.html', name='gmwang')


@app.route('/feifei')
def index_feifei():
    time.sleep(2)
    return render_template('index.html', name='feifei')


if __name__ == '__main__':
    app.run(debug=True)
