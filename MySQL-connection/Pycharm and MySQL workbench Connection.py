import mysql.connector as conn
#Establish communication between Pycharm and MySQL workbench

mydb = conn.connect(host = "localhost", user = "root", passwd = "mysql@DS")
cursor = mydb.cursor()
#cursor.execute("create database akriti")
#cursor.execute("show databases")
s = "create table akriti.akkiofficedetails1(employee_id int(10) , Employee_Name varchar(80), employee_email_id varchar(20), employee_salary int(8), employee_attendance int(3))"
#q1 = cursor.execute(s)

q2 = cursor.execute("select * from akriti.akkiofficedetails1")
print(q2)