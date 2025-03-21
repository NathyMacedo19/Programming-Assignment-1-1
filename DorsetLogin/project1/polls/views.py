from django.shortcuts import render

# needed imports
from tkinter import *
import tkinter as tk
import tkinter.messagebox
from django.db import connection
from MainMenu import *

import sqlite3 

# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# log in details

def login():
    global root2
    root2 = Toplevel(root)
    root2.title("Account Login")
    root2.geometry("450x300")
    root2.config(bg="pink")

    global username_verification
    global password_verification
    Label(root2, text='Enter your Log In Details', bd=5,font=('arial', 12, 'bold'), relief="groove", fg="white",
    bg="blue",width=300).pack()
    username_verification = StringVar()
    password_verification = StringVar()
    Label(root2, text="").pack()
    Label(root2, text="Username :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root2, textvariable=username_verification).pack()
    Label(root2, text="").pack()
    Label(root2, text="Password :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root2, textvariable=password_verification, show="*").pack()
    Label(root2, text="").pack()
    Button(root2, text="Login", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'),command=login_verification).pack()
    Label(root2, text="")

def login_verification(): # using mysql
    username = username_verification.get()
    password = password_verification.get()
    sql = "select * from logins where username = %s and password = %s"
    cursordb = connection.cursor()
    cursordb.execute(sql,[(username),(password)])
    results = cursordb.fetchall()
    if results:
        for i in results:
            logged()
            break
    else:
        failed()

# def login_verification(): # using sqllite
#     username = username_verification.get()
#     password = password_verification.get()
#     conn = sqlite3.connect('dorsetlogin.db')

#     cursordb = conn.cursor()
#     cursordb.execute("SELECT * from logins WHERE \
#                      name = :username and password = :password", 
#                      {"username": username, "password": password})
    
#     results = cursordb.fetchall()
#     conn.commit()
#     conn.close()

#     if results:
#         for i in results:
#             logged()
#             break
#     else:
#         failed()

def logged():
    global logged_message
    logged_message = Toplevel(root2)
    logged_message.title("Welcome")
    logged_message.geometry("500x100")
    Label(logged_message, text="Login Successful!... Welcome {} ".format(username_verification.get()), fg="green", font="bold").pack()
    Label(logged_message, text="").pack()
    Button(logged_message, text="Proceed", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'), command=mainmenuinstance).pack()

def mainmenuinstance():
    app = AccountsMenu(tk.Tk())
    app.initialize_user_interface()
    app.getdata()
    app.pulldownmenu(root)
    root.destroy()

def failed():
    global failed_message
    failed_message = Toplevel(root2)
    failed_message.title("Invalid Log In")
    failed_message.geometry("500x100")
    Label(failed_message, text="Invalid Username or Password", fg="red", font="bold").pack()
    Label(failed_message, text="").pack()
    Button(failed_message,text="Ok", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'), ).pack()

def Exit():
    wayOut = tkinter.messagebox.askyesno("Banking Application", "Do you want to exit?")
    if wayOut == 1 :
        root.destroy()
    return

def main_display():
    global root
    root = Tk()
    root.config(bg="pink")
    root.title("Login System")
    root.geometry("500x300")
    Label(root,text='Banking Application Log In', bd=20, font=('arial', 20, 'bold'), relief="groove", fg="white",
    bg="blue",width=300).pack()
    Label(root,text="").pack()
    Button(root,text='Log In', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
    bg="blue",command=login).pack()
    Label(root,text="").pack()
    Button(root,text='Exit', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
    bg="blue",command=Exit).pack()
    Label(root,text="").pack()

main_display()
root.mainloop()

