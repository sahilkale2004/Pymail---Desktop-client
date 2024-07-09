import tkinter as tk
from tkinter import ttk
import mysql.connector

def fetch_data():
    try:
        # Establish connection to MySQL database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="USER"
        )
        mycursor = mydb.cursor()

        # Execute query to retrieve data from the table
        mycursor.execute("SELECT email, password FROM signup")

        # Fetch all rows from the result set
        rows = mycursor.fetchall()

        return rows
    except mysql.connector.Error as e:
        print("Error fetching data:", e)
        return None

def display_data():
    # Fetch data from the database
    data = fetch_data()

    if data:
        # Clear existing data in the Treeview widget
        for row in table.get_children():
            table.delete(row)

        # Insert fetched data into the Treeview widget
        for row in data:
            table.insert('', 'end', values=row)

root = tk.Tk()
root.title('USERS DATA')
root.geometry('925x500')
root.configure(bg="#fff")
root.resizable(False, False)

# Treeview
table = ttk.Treeview(root, columns=('email', 'passwd'), show='headings')
table.heading('email', text='Email address')
table.heading('passwd', text='Password ')
table.column('email', width=400)
table.column('passwd', width=400)

# Pack the Treeview widget to fill the entire height of the window
table.pack(fill='both', expand=True)

# Connect to database and display data
display_data()

# Run the Tkinter main event loop
root.mainloop()
