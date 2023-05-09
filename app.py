from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<a href='/greet'>click me</a>"

@app.route("/greet")
def greet():
    return "<p>How are you?</p>"