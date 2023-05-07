import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Suresh@1702')
print(mydb.connection_id)
cur=mydb.cursor()
cur.execute("create database INVENTORY_MANAGEMENT")
