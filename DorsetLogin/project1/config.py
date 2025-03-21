import sys
from django.db import connections
from django.db.utils import OperationalError
from tkinter import *
import ctypes

import sqlite3 

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

class database:
    def connect_db():
        db_conn = connections['default']
        my_conn = db_conn.cursor()
    
    def connect_getaccount(my_conn):
        my_conn.execute("SELECT * FROM accounts")
    
    def connect_updatestudent(cursor, firstname, lastname, address, balance):
        cursor.execute('INSERT INTO accounts (firstname, lastname, address, balance) VALUES (%s,%s,%s,%s) ' , (firstname,lastname,address,balance))

    def dbsqllite():
        # connecting to sqllite3 database
        conn = sqlite3.connect('dorsetlogin.db') 
        cursordb = conn.cursor()

        # data=cursordb.execute('''SELECT * FROM logins''') 
        # for row in data: 
        #     print(row) 
        
        # Commit your changes in the database     
        conn.commit() 
        
        # # Closing the connection 
        # conn.close()
