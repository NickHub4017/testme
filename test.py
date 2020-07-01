import pymysql
import time
print("aaaaaaa")
while 1:
    # Open database connection
    print("bbbbb")
    db = pymysql.connect("database-3.ctvdurq9dsmz.us-east-2.rds.amazonaws.com","root","eranga19covid","covid_19" )
    print("ccccc")
    # prepare a cursor object using cursor() method
    cursor = db.cursor()
    print("dddddd")
    # execute SQL query using execute() method.
    cursor.execute("show tables")
    print("eeeeee")
    # Fetch a single row using fetchone() method.
    data = cursor.fetchall()
    print (data)

    # disconnect from server
    db.close()
    time.sleep(55)