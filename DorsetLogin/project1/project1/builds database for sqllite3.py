# script builds the login table and accounts table in sqlite3
# Import module 
import sqlite3 
  
# Connecting to sqlite 
conn = sqlite3.connect('dorsetlogin.db') 

# cursor object
cursordb = conn.cursor()

# Drop the tables if they already exist.
cursordb.execute("DROP TABLE IF EXISTS LOGINS")
cursordb.execute("DROP TABLE IF EXISTS ACCOUNTS")
  
# Creating table 
logins ="""CREATE TABLE logins(id int(10), name varchar(255), password varchar(255))"""
cursordb.execute(logins) 
  
# Queries to INSERT records. 
cursordb.execute('''INSERT INTO logins VALUES (1,'John Malone', '1234ezv')''') 

# create accounts table

accounts = """CREATE TABLE accounts (
  id int(11), firstname varchar(255), lastname varchar(255), address varchar(255),
  balance int(10))"""
cursordb.execute(accounts) 

# Queries to INSERT records. 
cursordb.execute('''INSERT INTO accounts VALUES (103, 'Bobby', 'Ewing', 'South Fork',2058)''') 
cursordb.execute('''INSERT INTO accounts VALUES (104, 'J.R.', 'Ewing', 'South Fork',5000)''') 

# Commit your changes in the database     
conn.commit() 
  
# Closing the connection 
conn.close()
