#!.venv/bin/python
from flask import Flask
from flask_app.movie.view import movie
from database import database

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')
    with app.app_context():
        database.init_db(app)
    app.register_blueprint(movie)
    return app


if __name__ == '__main__':
    create_app().run()