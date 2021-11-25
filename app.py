from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to the Index page"

@app.route("/Hi/")
def who():
    return "What is your name?"

@app.route("/hi/<username>")
def greet(username):
    return f"Hi there, {username}!"
