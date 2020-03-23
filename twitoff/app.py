# for app

from flask import Flask, render_template
from models import DB

# make our app factory

def create_app():
    app = Flask(__name__)


    # add config for database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite3.db'

    # have database know about the  app
    DB.init_app(app)

    @app.route('/')
    def root():
        return 'Welcome to Twitoff!'

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return 'Reset database!'
    return app
    