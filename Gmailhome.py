import tkinter as tk
from tkinter import Button, Canvas, PhotoImage
from PIL import Image, ImageTk


root = tk.Tk()
root.title('Home')
root.geometry('925x500+300+200')
root.resizable(False, False)
root.configure(background='white')

# Create and configure the label
label = tk.Label(root, text="Welcome to PYMAIL", font=('Calibri', 27), fg='black', bg='white')
label.pack(padx=0, pady=20)
label.place(x=110, y=200)

# Create and configure the Compose button
composebtn = Button(root, text='Compose Email', fg='black', bg='white', width=20, height=3, font=('Arial', 15),
                     borderwidth=0, highlightthickness=0)
composebtn.pack(pady=50, padx=60, anchor='s')  # Anchor the button to the south (bottom)
composebtn.place(x=70, y=320)

emailsentbtn = Button(root, text='Email Sent', fg='black', bg='white', width=20, height=3, font=('Arial', 15),
                      borderwidth=0, highlightthickness=0)
emailsentbtn.pack(pady=50, padx=60, anchor='s')  # Anchor the button to the south (bottom)
emailsentbtn.place(x=350, y=320)

emailreceivedbtn = Button(root, text='Email Received', fg='black', bg='white', width=20, height=3,
                          font=('Arial', 15), borderwidth=0, highlightthickness=0)
emailreceivedbtn.pack(pady=50, padx=60, anchor='s')  # Anchor the button to the south (bottom)
emailreceivedbtn.place(x=610, y=320)



# Create the home button with the logo and text
homebtn = Button(root, text='Home', fg='black', bg='white', width=20, height=3, font=('Arial', 15),  compound='left', borderwidth=0, highlightthickness=0)
homebtn.pack(pady=(10, 20), anchor='s')  # Anchor the button to the south (bottom)
homebtn.place(x=30, y=60)


# Create the profile button with the logo and text 
profilebtn = Button(root, text='Profile', fg='black', bg='white', width=20, height=3, font=('Arial', 15),  borderwidth=0, highlightthickness=0)
profilebtn.pack(pady=(10, 20), anchor='s')  # Anchor the button to the south (bottom)
profilebtn.place(x=650, y=60)

# Create a canvas for drawing the line
canvas = Canvas(root, width=900, height=2, bg='black', highlightthickness=0)
canvas.pack()
canvas.create_line(30, 80, 900, 80)  # Draw a line between the Home button and the label

root.mainloop()
