# include Flask class from file flask
from flask import Flask
from flask import escape

# create instance of Flask class, __name__ is predefined setup variable
myapp_obj = Flask(__name__)

# different URL the app will implement
@myapp_obj.route("/")
@myapp_obj.route("/index.html")
# called view function
def index():
    return "index!"

@myapp_obj.route("/hello")
def hello():
    return "Hello World!"

@myapp_obj.route("/login")
def login():
    return "Login Page!"

@myapp_obj.route("/members/<string:name>/")
def getMember(name):
    return escape(name)

myapp_obj.run()