# coding: utf-8
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('bootstrap1.html')

@app.route('/bootstrap.html')
def bs():
    return render_template('bs.html')

@app.route('/bootstrap-ja.html')
def bsja():
    return render_template('bsja.html')

if __name__ == '__main__':
    app.run()
