#!C:\Users\welcome\AppData\Local\Programs\Python\Python39\python
import cgi
import mysql.connector

print("Content-type: text/html")
print()

form=cgi.FieldStorage()
nm=form.getvalue("uid")
ps=form.getvalue("psw")

con=mysql.connector.connect(host="localhost",user="root",password="Bhushan@123",database="Dhanu")
curs=con.cursor()

curs.execute("select * from Dhanu where usefullnm='%s' and pswd='%s';" %(nm,ps))
rec=curs.fetchone()
if rec:
    
    print("<html>")
    print("<head>")
    print("<meta http-equiv='refresh' content='0; url=home.html'/>")
    print("</head>")
    print("</html>")
else:
    print("<h2 style='color:red'>Sorry Authentication Failde</h2>")
    print("<br><a href='index.html'>Home</a>")

    con.close()
