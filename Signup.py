from tkinter import *
from tkinter import messagebox
import mysql.connector
import os
from dotenv import load_dotenv

def open_login():
    root.destroy()
    os.system("python Loginpage.py")

def open_table_page():
    root.destroy()
    os.system("python Table.py")

def signup():
    email = user.get()
    password = code.get()
    confirm_password = confirm_code.get()

    if password == confirm_password:
        try:
            # Establish a connection to MySQL database
            mydb = mysql.connector.connect(
                host=os.getenv("HOST"),
                user=os.getenv("USER"),
                password=os.getenv("PASSWORD"),
                database=os.getenv("DATABASE")
            )
            mycursor = mydb.cursor()

            # Insert the user data into the table
            sql = "INSERT INTO signup (email, password) VALUES (%s, %s)"
            val = (email, password)
            mycursor.execute(sql, val)

            mydb.commit()

            messagebox.showinfo('Signup', 'Successfully signed up')

            # Open the table page
            open_table_page()

        except mysql.connector.Error as e:
            messagebox.showerror('Error', f"MySQL Error: {e}")

    else:
        messagebox.showerror('Invalid', "Passwords should match")

root = Tk()
root.title("SignUp")
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False, False)

img = PhotoImage(file="images/Signup.png")
Label(root, image=img, border=0, bg='white').place(x=50, y=90)

frame = Frame(root, width=350, height=390, bg='#fff')
frame.place(x=480, y=50)

heading = Label(frame, text='Sign up', fg="#57a1f8", bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    if user.get() == '':
        user.insert(0, 'Email')

user = Entry(frame, width=40, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Email')
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    if code.get() == '':
        code.insert(0, 'Password')

code = Entry(frame, width=30, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

def on_enter(e):
    confirm_code.delete(0, 'end')

def on_leave(e):
    if confirm_code.get() == '':
        confirm_code.insert(0, 'Confirm Password')

confirm_code = Entry(frame, width=30, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
confirm_code.place(x=30, y=220)
confirm_code.insert(0, 'Confirm Password')
confirm_code.bind("<FocusIn>", on_enter)
confirm_code.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

Button(frame, width=39, pady=7, text='Sign up', bg='#57a1f8', fg='white', border=0, command=signup).place(x=35, y=280)
label = Label(frame, text='I have an account', fg='black', bg='white', font=('Microsoft YaHeiUI Light', 9))
label.place(x=90, y=340)

signin = Button(frame, width=6, text='Sign in', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=open_login)
signin.place(x=200, y=340)

root.mainloop()

