from flask import Flask,render_template,request
import pymysql as sql
from flask_mail import Mail,Message
import os





app = Flask(__name__)


mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'simrangrover5@gmail.com'
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_HOST_PASSWORD')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

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
    try:
        db = sql.connect(host="localhost",port=3306,user="root",password="",database="batch2pm")
    except:
        return "Connectivity Error...."
    else:
        c = db.cursor()
        c.execute(f"select * from user where email='{email}'")
        data = c.fetchone()
        if data:
            #print(data)
            if password == data[2]:
                return render_template("one.html")
            else:
                error = "Invalid password"
                return render_template("login.html",error=error)
        else:
            error = "No such user...."
            return render_template("login.html",error=error)
    return f"Email {email} and password {password}"

@app.route("/signup/")
def signup():
    return render_template("signup.html")

@app.route("/aftersignup/",methods=['POST'])
def signup1():
    email = request.form.get('email')
    password = request.form.get('pswd')
    username = request.form.get('uname')
    gender = request.form.get('gender')
    try:
        db = sql.connect(host="localhost",port=3306,user="root",password="",database="batch2pm")
    except:
        return "Connectivity Error...."
    else:
        c = db.cursor()
        c.execute(f"select * from user where email = '{email}'")
        data = c.fetchone()
        print(data)
        if data:
            error = "User already exist....."
            return render_template("signup.html",error=error)
        else:
            cmd = f"insert into user values('{username}','{email}','{password}','{gender}')"
            c.execute(cmd)
            db.commit()
            return render_template("login.html")

@app.route("/contact/")
def contact():
    #to = "bhattjagdish1994@gmail.com"
    body = """This is a message to all the students who dont't study....
    If they will not study they will not get job and all there money will be wasted.."""
    m = Message(subject="Mail from flask app",recipients=["simrangrover5@gmail.com"],body=body,sender="simrangrover5@gmail.com")
    mail.send(m)
    return "SUCCESS"

app.run(host="localhost",port=80,debug=True)
