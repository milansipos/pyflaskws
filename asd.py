from flask import Flask, request, render_template, jsonify
from markupsafe import escape
import time

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")


@app.route("/milan")
def milan():
    return "<p>Hello, Milan!</p>"

@app.route("/test/<name>")
def hello(name):
    return "Hello, " + escape(name) + "!"

@app.route("/button")
def button():
    print("button clicked")
    data = {"data":"myvalue", "hello":"hellovalue"}
    return data

@app.route("/login")
def loggingin():
    return """
    <nav> Back home: <a href="/"><button>Home</button></a>
    <form action=/loggedin  method="POST">
    <input type="text" name="username" placeholder="Username">
    <input type="password" name="password" placeholder="Password">
    <button type="submit">Login</button> 
    </form>
    """

@app.route("/loggedin", methods=["POST"])
def login():
    username = request.form.get("username", "Guest")
    password = request.form.get("password", "")
    return f"""
    <nav> Back home: <a href="/"><button>Home
    </button></a>
    User {username} logged in!
    """