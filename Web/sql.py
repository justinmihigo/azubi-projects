import mysql.connector
db=mysql.connector.connect(host='localhost',user='root',passwd='12345',port='8800',database='justin')
print(db)
curs=db.cursor()
sql="INSERT INTO STUDENT VALUES(%s,%s,%s)"
val=[("RUGWIRO",10,"MPC"),
("JULIEN",11,"MPG"),
("KIK",89,"PCM")
]

curs.executemany(sql,val)
db.commit()
print(curs.rowcount," rows inserted")
curs.execute("SELECT * FROM STUDENT")
result=curs.fetchall()
for x in result:
    print(x)
