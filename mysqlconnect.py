import pymysql as sql


db = sql.connect(host="localhost",port=3306,user="root",password="",database="batch2pm")

cursor = db.cursor()


cmd = "select * from student"
cursor.execute(cmd)

data = cursor.fetchall()
#print(data)
for i in data:
    print("Id : ",i[0])
    print("Name : ",i[1])
    print("Course : ",i[2])
    print("Age : ",i[3])
    print()


print("Done")
