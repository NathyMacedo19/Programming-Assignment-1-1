from tkinter import *
from django.db import connection
import ctypes  # An included library with Python install.
import config # import global variables for form
from config import database

def updatedatabase():
    mydb = database.connect_db()
    my_conn = connection.cursor()
    database.connect_updatestudent(my_conn, config.firstname.get(), config.lastname.get(), config.address.get(), config.balance.get())
    root.destroy()
    database.connect_getaccount(my_conn)

def login():
    ## Use of global variables makes them available in all functions
    global root
    root=Tk()
    root.title("Dorset Bank Database")
    root.geometry("450x350")
    root.config(bg="pink")
    root.resizable(0,0)

    Label(root, text='Please Enter your account details', bd=5,font=('arial', 12, 'bold'), relief="groove", fg="white",
    bg="blue",width=300).pack()

    # added root to StringVar to get form working properly
    config.firstname = StringVar(root)
    config.lastname = StringVar(root)
    config.address = StringVar(root)
    config.balance = StringVar(root)

    Label(root, text="").pack()
    Label(root, text="Firstname :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root, textvariable=config.firstname).pack()
    Label(root, text="Lastname :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root, textvariable=config.lastname).pack()
    Label(root, text="Address :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root, textvariable=config.address).pack()
    Label(root, text="").pack()
    Label(root, text="Balance :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root, textvariable=config.balance).pack()
    Label(root, text="").pack()

    Button(root, text="Store to Dbase", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'), command=updatedatabase).pack()
    Button(root, text="Exit", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'), command=Exit).pack()

    Label(root, text="")

    root.mainloop()

def Exit():
    wayOut = Mbox('Student Database', 'Do you want to exit?', 1)
    if wayOut == 1 :
        root.destroy()
    return

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)
