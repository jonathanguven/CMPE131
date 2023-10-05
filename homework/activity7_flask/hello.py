from flask import Flask # include the flask module from installed Flask file
from datetime import datetime

app = Flask(__name__) # Create instance of Flask class, where __name__ is the default setup variable

# Create a website URL route called "/hello"
@app.route("/hello")
# This creates view function called hello() which is decorated by @app.route("/hello")
def hello():
    return "Hello CMPE 131!" # The function returns what you will see on the web page

@app.route('/<name>')
def hello_name(name):
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f"""
    <html>
        <head>
            <title>Home Page - my blog</title>
        </head>
        <body>
            <h1>Hello, {name} !</h1>
            <b> Today is {current_datetime} </b>
        </body>
    </html>
    """

app.run() # app.run() runs the flask application on the host server

# Once running, you can visit http://127.0.0.1:5000/hello in a web browser to see the output "Hello CMPE 131!".