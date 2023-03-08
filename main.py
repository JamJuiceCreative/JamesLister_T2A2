# import area
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.app_config")
    db.init_app(app)
    from controllers import registerable_controllers
    for controller in registerable_controllers:
        app.register_blueprint(controller)
    return app

# #initial stage for connecting to local host
# @app.route("/")
# def connect():
#     return "Project is connected to local host!!!"