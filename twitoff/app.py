from flask import Flask, render_template

"""Create and congifure Flask application"""
app = Flask(__name__)

@app.route('/')
def hello():
    print('Visited hello world page')
    return "Hello Twitoff! Is anybody out there?"


# Make a second route
@app.route("/about")
def about():
    """ Function that goes with about"""
    print("Visited the about page")
    return "About Me!"