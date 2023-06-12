import mysql.connector as conn

mydb = conn.connect(host = "localhost", user = "root", passwd = "mysql@DS")
cursor = mydb.cursor()
s = "insert into akriti.akkiofficedetails1 values (101, 'Akriti Singh' , 'akriti@gmail.com' , 500000, 30)"
cursor.execute(s)

mydb.commit()  # when inserting data in table commit command is required

cursor.execute("select * from akriti.akkiofficedetails1")
for i in cursor.fetchall():
    print(i)