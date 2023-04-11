from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home(name=None):
    return render_template('index.html', name=name)


@app.route("/blog")
def blog(name=None):
    return render_template('blog.html', name=name)


@app.route("/cars")
def cars(name=None):
    return render_template('cars.html', name=name)


@app.route("/messages")
def messages(name=None):
    return render_template('messages.html', name=name)


@app.route("/abaut")
def abaut(name=None):
    return render_template('abaut.html', name=name)


@app.route("/login")
def login(name=None):
    return render_template('login.html', name=name)

@app.route("/greet/<name>/")
def greet_name(name: str):
    return f"Hello {name}!"
