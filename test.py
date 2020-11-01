##https://www.datacamp.com/community/tutorials/mysql-python

import pandas as pd
import mysql.connector as mysql
from sqlalchemy import create_engine

## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'

#database_table ="monitor"
host = 'localhost'
user = 'xxxxx'
passwd = 'xxxxx'
port = '3306'
database_name = 'computer'
database_table = 'monitor'


db = mysql.connect(host = host,user = user,passwd = passwd,port = port)
cursor = db.cursor()

if db.is_connected():
    db_Info = db.get_server_info()
    print("Connected to MySQL Server version ", db_Info)
    cursor = db.cursor()

#create database
cursor.execute("CREATE DATABASE IF NOT EXISTS computer")

db = mysql.connect(
    host = "localhost",
    user = "xxxxx",
    passwd = "xxxxx",
    port = '3306',
    database = "computer",
    )
cursor = db.cursor()
## creating the  table  with the 'PRIMARY KEY'
cursor.execute("CREATE TABLE IF NOT EXISTS monitor (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), user_name VARCHAR(255))")

import pandas as pd
import mysql.connector
from sqlalchemy import types, create_engine

# MySQL Connection
MYSQL_USER 		= 'xxxxxx'
MYSQL_PASSWORD 	= 'xxxxxx'
MYSQL_HOST_IP 	= 'localhost'
MYSQL_PORT		= '3306'
MYSQL_DATABASE	= 'computer'

engine = create_engine('mysql+mysqlconnector://'+MYSQL_USER+':'+MYSQL_PASSWORD+'@'+MYSQL_HOST_IP+':'+MYSQL_PORT+'/'+MYSQL_DATABASE, echo=False)
cursor.execute("CREATE TABLE IF NOT EXISTS monitor (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), user_name VARCHAR(255))")

# printing data frame
data = pd.read_excel (r'/home/vikram/Documents/test.xlsx')   
df = pd.DataFrame(data)
print(df)
# Convert dataframe to sql table                                   
df.to_sql('monitor', con=engine,if_exists='replace')


