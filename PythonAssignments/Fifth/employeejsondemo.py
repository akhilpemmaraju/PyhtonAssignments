import json
import pymysql
db = pymysql.connect("localhost","root","","test" )
cursor = db.cursor(pymysql.cursors.DictCursor)
fo=open('jsondata.txt','r')
li=json.load(fo)
for d in li:
    f = d["fname"]
    l = d["lname"]
    sql = "INSERT INTO Employee (fname, lname) VALUES (%s, %s)"
    val = (f, l)
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "record inserted.")
fo.close()