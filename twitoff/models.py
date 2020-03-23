from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

# Each class we make will be a table in the DB
class User(DB.Model):
    """ TWITTER USERS we analyze"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)

class Tweet(DB.Model):
    """TWEETS we pull"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(280))