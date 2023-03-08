from flask import Flask
app = Flask(__name__)

@app.route("/")
def connect():
    return "Project is connected to local host!!!"