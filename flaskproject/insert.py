import pymysql as sql


db = sql.connect(host="localhost",port=3306,user="root",password="",database="batch2pm")
c = db.cursor()

for i in range(10):
    try:
        id1 = int(input("ENter your id : "))
        title = input("Enter title : ")
        ratings = float(input("Enter rating out of 5 : "))
        genre = input("Enter genre : ")
        cmd = f"insert into movie values({id1},'{title}',{ratings},'{genre}')"
        c.execute(cmd)
        db.commit()
        print("\n Data inserted......")
    except:
        pass