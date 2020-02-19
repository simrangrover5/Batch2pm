from flask import Flask,render_template,request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("nav.html")
    #return "hello world"


@app.route("/home/<var>/")
def home(var):
    return render_template("one.html",name=var)
    #return "<h1 style='color:blue'>Welcome to my home of python</h1>"

@app.route("/home/<var>/<int:m1>/<int:m2>/<int:m3>/")
def name(var,m1,m2,m3):
    d = {
        'name':var,
        'science':m1,
        'maths':m2,
        'english':m3
    }
    return render_template("one.html",data=d)
    #return f"<h1 style='color:red;font-style:italic'>Your subject is {var} and your marks is {m}</h1>"


@app.route('/login/')
def login():
    return render_template("login.html")


@app.route("/afterlogin/",methods=['POST'])
def afterlogin():
    email = request.form.get('email')
    password = request.form['pswd']
    return f"Email {email} and password {password}"

@app.route("/signup/")
def signup():
    return render_template("signup.html")

app.run(host="localhost",port=80,debug=True)
