# creating goods table
import mysql.connector
mydb = mysql.connector.connect(
    host='localhost', user='root', password='Suresh@1702', database='INVENTORY_MANAGEMENT')
cur = mydb.cursor()
tb = 'CREATE TABLE GOODS(GOODS_ID INT NOT NULL, NUMBER_ITEMS INT NOT NULL, MANUFACTURE_DATE DATE NOT NULL, PRODUCT_NAME VARCHAR(20) NOT NULL,COLOR VARCHAR(20) NOT NULL, PRIMARY KEY(PRODUCT_NAME, COLOR), FOREIGN KEY(MANUFACTURE_DATE) REFERENCES MANUFACTURE(MANUFACTURE_DATE) ON DELETE CASCADE)'
cur.execute(tb)

# creating manufacture table

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost", user="root", password="Suresh@1702", database="INVENTORY_MANAGEMENT")
cur = mydb.cursor()
t = 'CREATE TABLE MANUFACTURE(MANUFACTURE_ID INT NOT NULL,MANUFACTURE_COMPANY VARCHAR(20),DEFECTIVE BIT NOT NULL,NUMBER_ITEMS INT NOT NULL,MANUFACTURE_DATE DATE PRIMARY KEY NOT NULL,PRODUCT_NAME VARCHAR(20) NOT NULL,COLOR VARCHAR(10) NOT NULL)'
cur.execute(t)

# creating purchase table

import mysql.connector
my_db = mysql.connector.connect(host='localhost', user='root',
                                password='Suresh@1702', database='INVENTORY_MANAGEMENT')
cur = my_db.cursor()
t = 'CREATE TABLE PURCHASE(PURCHASE_ID INT PRIMARY KEY NOT NULL,STORE_MODE VARCHAR(40) NOT NULL,PRODUCT_NAME VARCHAR(20) NOT NULL,COLOR VARCHAR(10) NOT NULL,NUMBER_ITEMS INT NOT NULL,PURCHASE_DATE DATE NOT NULL,PURCHASE_AMOUNT FLOAT NOT NULL);'
cur.execute(t)

# creating sales table

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost", user="root", password="Suresh@1702", database="INVENTORY_MANAGEMENT")
cur = mydb.cursor()
t = "CREATE TABLE SALE(SALE_ID INT PRIMARY KEY NOT NULL,STORE_NAME VARCHAR(40) NOT NULL,SALE_DATE DATE NOT NULL,COLOR VARCHAR(10) NOT NULL,NUMBER_ITEMS INT NOT NULL,PRODUCT_NAME VARCHAR(20) NOT NULL,SALE_AMOUNT FLOAT NOT NULL,PROFIT_MARGIN FLOAT,FOREIGN KEY(PRODUCT_NAME, COLOR) REFERENCES GOODS(PRODUCT_NAME, COLOR) ON DELETE CASCADE)"
cur.execute(t)
