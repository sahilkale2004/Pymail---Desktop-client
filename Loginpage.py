from tkinter import *
from tkinter import messagebox
import os
import subprocess
import mysql.connector
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def open_signup():
    root.destroy()
    os.system("python signup.py")

def fetch_data(email, password):
    try:
        # Establish connection to MySQL database
        mydb = mysql.connector.connect(
            host=os.getenv("HOST"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            database=os.getenv("DATABASE")
        )
        mycursor = mydb.cursor()

        # Execute query to check if email and password match a record
        mycursor.execute("SELECT * FROM signup WHERE email = %s AND password = %s", (email, password))
        row = mycursor.fetchone()
        return row

    except mysql.connector.Error as e:
        print("Error fetching data:", e)
        return None

def Login():
    email = user.get()
    password = code.get()

    row = fetch_data(email, password)

    if row:
        root.destroy()
        subprocess.Popen(["python", "home.py"])
    else:
        messagebox.showerror("Invalid", "Invalid email and password")

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

img = PhotoImage(file="images/login.png")
Label(root, image=img, bg='white').place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text='Login', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

def on_email_enter(e):
    if user.get() == 'Email':
        user.delete(0, 'end')

def on_email_leave(e):
    if user.get() == '':
        user.insert(0, 'Email')

user = Entry(frame, width=40, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Email')
user.bind('<FocusIn>', on_email_enter)
user.bind('<FocusOut>', on_email_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

def on_pass_enter(e):
    if code.get() == 'Password':
        code.delete(0, 'end')

def on_pass_leave(e):
    if code.get() == '':
        code.insert(0, 'Password')

code = Entry(frame, width=30, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_pass_enter)
code.bind('<FocusOut>', on_pass_leave)
Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=Login).place(x=35, y=204)
label = Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=75, y=270)

sign_up = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=open_signup)
sign_up.place(x=215, y=270)

root.mainloop()