import sqlite3 as sql



db = sql.connect("student.db")
cursor = db.cursor()

#cmd = "create table student(id int(5),name varchar(100),course varchar(100))"

#cursor.execute(cmd)

while True:
    id1 = int(input("Enter your id : "))
    name = input("Enter your name : ")
    course = input("Enter your course : ")

    cmd = f"insert into student values({id1},'{name}','{course}')"
    cursor.execute(cmd)
    db.commit()

    print("Data inserted successfully")
    ch = input("Do you want to continue or not(yes/no) : ").strip().lower()
    if ch == "no":
        print("Bye bye....")
        break
