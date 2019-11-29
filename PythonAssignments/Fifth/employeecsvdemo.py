import csv
import pymysql
db = pymysql.connect("localhost","root","","test" )
cursor = db.cursor(pymysql.cursors.DictCursor)
reader = csv.reader(open('data.csv','r'),delimiter=',')
for data in reader:
    f=data[0]
    l=data[1]
    sql = "INSERT INTO Employee (fname, lname) VALUES (%s, %s)"
    val = (f, l)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "record inserted.")

db.close()