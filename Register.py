#!C:\Users\welcome\AppData\Local\Programs\Python\Python39\python
import cgi
import mysql.connector
print("Content-type: text/html")
print()

request=cgi.FieldStorage()
nm=request.getvalue("ufnm")
ps=request.getvalue("psw")
ag=int(request.getvalue("age"))
ct=request.getvalue("ct")
mo=request.getvalue("mob")



con=mysql.connector.connect(host='localhost',user='root',password='Bhushan@123',database='Dhanu')
curs=con.cursor()

try:
    curs.execute("insert into Dhanu values('%s','%s','%d','%s','%s');"%(nm,ps,ag,ct,mo))
    con.commit()
    print("<h1 style='color:green'> Candidate Registration Successful </h1>")
except:
    print("<h1 style='color:red'>Registration Failed......</h1>")

con.close()
print("<br><br><a href='index.html'>Home</a>")
