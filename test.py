import pymysql
import time

while 1:
    # Open database connection
    db = pymysql.connect("database-3.ctvdurq9dsmz.us-east-2.rds.amazonaws.com","root","eranga19covid","covid_19" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # execute SQL query using execute() method.
    cursor.execute("show tables")

    # Fetch a single row using fetchone() method.
    data = cursor.fetchall()
    print (data)

    # disconnect from server
    db.close()
    time.sleep(55)