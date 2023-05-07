#Update the manufacture details of all the red-colored toys which are purchased by the “MyKids” store.

import mysql.connector
mydb = mysql.connector.connect(
    host='localhost', user='root', password='Suresh@1702', database='INVENTORY_MANAGEMENT')
cur = mydb.cursor()update='UPDATE MANUFACTURE SET NUMBER_ITEMS=10 WHERE PRODUCT_NAME="TOY CAR" AND COLOR="RED"';
cur.execute(update);
print("Updated Successfully");
