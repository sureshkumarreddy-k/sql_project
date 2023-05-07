#Display the profit margin amount of the “wooden table” that was sold by the “MyCare” store, manufactured by the “SS Export” company.
import mysql.connector
mydb = mysql.connector.connect(
    host='localhost', user='root', password='Suresh@1702', database='INVENTORY_MANAGEMENT')
cur = mydb.cursor()
show='SELECT S.PROFIT_MARGIN FROM MANUFACTURE M,SALE S WHERE M.MANUFACTURE_COMPANY="SS EXPORT" AND M.PRODUCT_NAME="WOODEN TABLE" AND S.STORE_NAME="MY CARE"';
show=cur.execute(show);
display=cur.fetchall()
print("values are:");
for value in display:
    print(value);
