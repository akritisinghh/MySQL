import mysql.connector as conn

mydb = conn.connect(host = "localhost", user = "root", passwd = "mysql@DS")
cursor = mydb.cursor()
cursor.execute("select employee_id, employee_email_id from akriti.akkiofficedetails1")
l = []
for i in cursor.fetchall():
   l.append(i)

print(l)
print(type(l[0]))