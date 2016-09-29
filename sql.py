#!/usr/bin/python

print "starting sql.py"

import MySQLdb
import pandas as pd

holder = pd.read_csv('EWSeason.csv', header=None)
seasons = holder.values


# Open database connection
db = MySQLdb.connect("localhost","root","radnmo9","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS EARNEDWINS3")

# Create table as per requirement
#sql = """CREATE TABLE EMPLOYEE2 (
#         FIRST_NAME  CHAR(20) NOT NULL,
#         LAST_NAME  CHAR(20),
#         AGE INT,
#         SEX CHAR(1),
#         INCOME FLOAT )"""


sql = """CREATE TABLE EARNEDWINS3 (
        ID int AUTO_INCREMENT PRIMARY KEY,
        NAME VARCHAR (32),
        TEAM VARCHAR(16),
        YEAR INT,
        STARTS INT,
        IP FLOAT(6,2),
        ERA FLOAT(5,2),
        EWA FLOAT(2,2),
        W INT,
        L INT,
        EW FLOAT(4,2),
        EL FLOAT(4,2),
        SUPPORT FLOAT(4,2) )"""

cursor.execute(sql)

for x in range (len(seasons)):
    print x
    if x == 0:
       continue
    sql_command = """INSERT INTO EARNEDWINS3 (ID, NAME, TEAM, YEAR, STARTS, IP, ERA, EWA, W, L, EW, EL, SUPPORT)
        VALUES (NULL, "{a0}", "{a1}", {a2}, {a3}, {a4}, {a5}, {a6}, {a7}, {a8}, {a9}, {a10}, {a11});"""
    name = seasons[x][0]
    sql_command = sql_command.format(a0=name, a1=seasons[x][1], a2=seasons[x][2], a3 = seasons[x][3], a4=seasons[x][4], a5=seasons[x][5], a6=seasons[x][6], a7=seasons[x][7], a8=seasons[x][8], a9=seasons[x][9], a10=seasons[x][10], a11=seasons[x][11])
    print "about to execute"
    print sql_command
    cursor.execute(sql_command)


db.commit()
# disconnect from server
db.close()


cursor.close()