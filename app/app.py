"""Flask application for CPS3500 assignment."""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """Display the default homepage message."""
    return "Hello CPS3500!"

@app.route('/new_page')
def new_page():
    """Display the new page message."""
    return "This is a New Page!"

@app.route('/user/<username>')
def user(username):
    """Render a template greeting based on the username."""
    return render_template('user.html', username=username)

if __name__ == '__main__':
    app.run()
