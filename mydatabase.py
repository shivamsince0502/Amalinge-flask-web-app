

import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="", database="codethunder")
cursor = con.cursor()
query1 = "desc contact"
cursor.execute(query1)
table = cursor.fetchall()
print('\n Table Description: ')
for atr in table:
    print(atr)

query2 = "select * from contact"

cursor.execute(query2)
table=cursor.fetchall()

print('\n Table Data')
for row in table:
    l1 = list(row[2])
    l2 = list(row[3])
for l in l1:
    print(l)
for w in l2:
    print(w)

cursor.close()
con.close()