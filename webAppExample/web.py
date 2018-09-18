from flask import Flask, render_template

app = Flask(__name__)


@app.route("/saludo")
def hello():
    return "Hello World!"


@app.route("/")
def main():
    return render_template('index.html')
