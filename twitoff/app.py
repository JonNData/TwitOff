# for app

from flask import Flask, render_template
from .models import DB, User

# app.py should just have app configuration and routing logic


def create_app():
    """ Create and configure an instance of the flask app"""
    app = Flask(__name__)

    # add config for database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite3.db'

    # have database know about the  app
    DB.init_app(app)

    @app.route('/')
    @app.route('/home')
    def home():
        users = User.query.all()
        return render_template('home.html', title='Home', users=users)

    @app.route('/about')
    def about():
        return '<h1>About Page</h1><p>Just trying to compare tweet behaviours!</p>'

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return 'Reset database!'
    return app


if __name__ == "__main__":
    app = Flask(__name__)
    app.run(debug=True)
