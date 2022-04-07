#!C:\Users\91971\AppData\Local\Programs\Python\Python310\python.exe
print('Content-Type:text/html')
print()
import cgitb,cgi
cgitb.enable()

data=cgi.FieldStorage()

uname=data.getvalue('name')
ugender=data.getvalue('gender')
unumber=data.getvalue('number')
ucar=data.getvalue('cars')

print('<html>')
print('<head>')
print('<title>User Data</title>')
print('</head>')
print('<body>')
print('<b>Name: </b>{name}'.format(name=uname))
print('<br>')
print('<b>Gender: </b>{gender}'.format(gender=ugender))
print('<br>')
print('<b>Number: </b>{number}'.format(number=unumber))
print('<br>')
print('<b>Car: </b>{car}'.format(car=ucar.upper()))
print('</body>')
print('</html>')








