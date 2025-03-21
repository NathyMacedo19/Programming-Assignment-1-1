import sys
import tkinter as tk
import tkinter.ttk as ttk
from django.db import connection
from tkinter import Menu
import config # import global variables for form
from config import database

from CreateAccount import *  # imports everything from CreateAccount file

import sqlite3

class AccountsMenu(tk.Frame):
    def __init__(self, root):
        self.root = root
        self.initialize_user_interface()
        self.getdata()
        self.pulldownmenu(root)

    def pulldownmenu(self,root):
        ## File Pull down menu
        menu = Menu(root)
        root.config(menu=menu) # this adds menu bar to frame
        new_file1 = Menu(menu, tearoff=0)
        menu.add_cascade(label='File', menu=new_file1)
        new_file1.add_command(label='Refresh', command=self.insert_data)
        new_file1.add_command(label='Exit Application', command=self.root.destroy)

        ## Edit Pull Down Menu
        new_edit1 = Menu(menu, tearoff=0)
        menu.add_cascade(label='Edit', menu=new_edit1)
        new_edit1.add_command(label='Create Account', command=login )
        new_edit1.add_command(label='Delete Account', )
        new_edit1.add_command(label='Edit Account', )
        new_edit1.add_command(label='Transfer Funds', )
        new_edit1.add_command(label='Withdraw Funds', )
        new_edit1.add_command(label='Deposit Funds', )
        new_edit1.add_command(label='View Transactions', )

    def initialize_user_interface(self):

        # Configure the root object for the Application
        self.root.title("Banking Application")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(4, weight=1)
        self.root.config(background="lightblue")
        self.root.resizable(0,0)
        
        # Set the treeview
        self.tree = ttk.Treeview(self.root, columns=('Id', 'Firstname','Lastname','Address','Balance'))

        # Set the heading (Attribute Names)
        self.tree.heading('#1', text='Id')
        self.tree.heading('#2', text='Firstname')
        self.tree.heading('#3', text='Lastname')
        self.tree.heading('#4', text='Address')
        self.tree.heading('#5', text='Balance')

        # Specify attributes of the columns (We want to stretch it!)
        self.tree.column('#1', width=100, stretch=tk.NO)
        self.tree.column('#2', width=200, stretch=tk.NO)
        self.tree.column('#3', width=200, stretch=tk.NO)
        self.tree.column('#4', width=200, stretch=tk.NO)
        self.tree.column('#5', width=100, stretch=tk.NO)

        self.tree.column("#0", width=0)

        self.tree.grid(row=4, columnspan=4, sticky='nsew')
        self.treeview = self.tree

        self.id = 0
        self.iid = 0

    def getdata(self): # using mysql
        mydb = database.connect_db()
        my_conn = connection.cursor()
        database.connect_getaccount(my_conn)
        rows = my_conn.fetchall()
        for student in rows:
            self.treeview.insert('', 'end', values=student)
    
    # def getdata(self): # using sqllite
    #     conn = sqlite3.connect('dorsetlogin.db')
    #     cursordb = conn.cursor()
    #     data=cursordb.execute('''SELECT * FROM accounts''')
    #     data = cursordb.fetchall()
    #     for student in data:
    #         self.treeview.insert('', 'end', values=student)

    def delete_data(self):
        row_id = self.tree.focus()
        row_id = self.tree.item(row_id)['values'][0]
        id = (row_id, )

        mydb = database.connect_db()
        mycursor = connection.cursor()
        id = (row_id, )
        database.connect_deletestudent(mycursor,id)
                
        ## refresh table
        for i in self.tree.get_children():
            self.tree.delete(i)
        my_conn = connection.cursor()
        database.connect_getstudent(my_conn)
        rows = my_conn.fetchall()
        for student in rows:
            self.treeview.insert('', 'end', values=student)

    def insert_data(self):
        my_conn = connection.cursor()

        for i in self.tree.get_children():
            self.tree.delete(i)
        database.connect_getaccount(my_conn)
        rows = my_conn.fetchall()
        for student in rows:
            self.treeview.insert('', 'end', values=student)
