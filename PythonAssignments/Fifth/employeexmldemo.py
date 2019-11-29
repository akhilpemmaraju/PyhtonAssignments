import xml.dom.minidom
import pymysql
db = pymysql.connect("localhost","root","","test" )
cursor = db.cursor(pymysql.cursors.DictCursor)
lixmlempl=[]
# Open XML document using minidom parser
root = xml.dom.minidom.parse("employees.xml")
employees = root.documentElement
if employees.hasAttribute("org"):
    print("Root element : %s" % employees.getAttribute("org"))

for employee in employees.getElementsByTagName('employee'):
    fname = employee.getElementsByTagName('fname')[0]
    f = fname.childNodes[0].data
    lname = employee.getElementsByTagName('lname')[0]
    l = lname.childNodes[0].data
    sql = "INSERT INTO Employee (fname, lname) VALUES (%s, %s)"
    val = (f, l)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "record inserted.")
    lixmlempl.append({"fname": f, "lname": l})

db.close()
