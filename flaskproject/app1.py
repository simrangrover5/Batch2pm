from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"


@app.route("/home/")
def home():
    return "<h1 style='color:blue'>Welcome to my home of python</h1>"

@app.route("/home/<var>/<int:m>")
def name(var,m):
    return f"<h1 style='color:red;font-style:italic'>Your subject is {var} and your marks is {m}</h1>"

app.run(host="localhost",port=80,debug=True)
