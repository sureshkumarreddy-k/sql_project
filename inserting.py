# inserting values into goods table

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost", user="root", password="Suresh@1702", database="INVENTORY_MANAGEMENT")
cur = mydb.cursor()
insert = 'INSERT INTO goods (GOODS_ID, PRODUCT_NAME, COLOR, NUMBER_ITEMS, MANUFACTURE_DATE) values(%s,%s,%s,%s,%s)'
data = [(1, 'Toy Car', 'Blue', 100, '2023-04-01'),
        (2, 'Toy Car', 'Red', 50, '2023-04-03'),
        (3, 'Wooden Chair', 'Brown',200, '2023-03-01'),
        (4, 'Wooden Chair', 'White', 150, '2023-03-15')
        (5, 'Teddy Bear', 'Pink', 300, '2023-05-01')]
cur.executemany(insert, data)
mydb.commit()


# inserting into manufacture table


import mysql.connector
mydb = mysql.connector.connect(
    host="localhost", user="root", password="Suresh@1702", database="INVENTORY_MANAGEMENT")
cur = mydb.cursor()
z = 'INSERT INTO manufacture (MANUFACTURE_ID,MANUFACTURE_COMPANY, PRODUCT_NAME, COLOR, NUMBER_ITEMS, MANUFACTURE_DATE, DEFECTIVE) VALUES(%s,%s,%s,%s,%s,%s,%s)'
a = [(1, 'SS EXPORT', 'Toy Car', 'Blue', 100, '2023-04-01', 0), (2, 'SG EXPORT', 'Toy Car', 'Red', 50, '2023-04-03', 1), (3, 'SS EXPORT', 'Wooden Chair','Brown', 200, '2023-03-01', 1), (4, 'SRS EXPORT', 'Wooden Chair', 'White', 150, '2023-03-15', 0), (5, 'XYZ EXPORT', 'Teddy Bear', 'Pink', 300, '2023-05-01', 1)]
cur.executemany(z, a)
mydb.commit()

# inserting into purchase table

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost", user="root", password="Suresh@1702", database="INVENTORY_MANAGEMENT")
cur = mydb.cursor()
insert='INSERT INTO purchase (PURCHASE_ID, STORE_MODE, PRODUCT_NAME, COLOR, NUMBER_ITEMS, PURCHASE_AMOUNT, PURCHASE_DATE) VALUES(%s,%s,%s,%s,%s,%s,%s)'
values=[(1, 'Online Store', 'Toy Car', 'Blue', 50, 1000, '2023-04-05'),
       (2, 'Offline Store', 'Wooden Chair', 'Brown', 20, 3000, '2023-04-10'),
       (3, 'Online Store', 'Teddy Bear', 'Pink', 100, 2000, '2023-05-02')]
cur.executemany(insert,values)

# inserting into sale table

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost", user="root", password="Suresh@1702", database="INVENTORY_MANAGEMENT")
cur = mydb.cursor()
z = "INSERT INTO sale(SALE_ID, STORE_NAME, PRODUCT_NAME, COLOR, NUMBER_ITEMS, SALE_AMOUNT, PROFIT_MARGIN, SALE_DATE) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
a = [
    (1, 'MyCare', 'Wooden Chair', 'Brown', 10, 5000, 1000, '2023-04-20'),
    (2, 'ORay', 'Teddy Bear', 'Pink', 5, 500, 100, '2023-04-15'),
    (3, 'MyKids', 'Toy Car', 'Red', 30, 1500, 300, '2023-05-01')
]
cur.executemany(z, a)
mydb.commit()

