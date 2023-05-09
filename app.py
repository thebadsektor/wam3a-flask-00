from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<a href='/greet'>click me</a>"

@app.route("/greet")
def greet():
    return "<p>How are you?</p>"

@app.route("/knock-knock")
def knock_knock():
    return "<p>Who's there?</p>"

@app.route("/end")
def end():
    return "<p>Hello Love Good Boy</p>"

