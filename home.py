import tkinter as tk
import subprocess

# Initialize main window
root = tk.Tk()
root.title("PyMail Dashboard")
root.geometry("400x300")
root.configure(bg="white")
root.resizable(False, False)

# Title label
tk.Label(
    root,
    text="📬 Welcome to PyMail",
    font=("Segoe UI", 18, "bold"),
    fg="#57a1f8",
    bg="white"
).pack(pady=25)

# Launch Compose Module
def open_compose():
    subprocess.Popen(["python", "compose.py"])

# Launch Inbox Module
def open_inbox():
    subprocess.Popen(["python", "inbox.py"])

# Launch Admin Panel
def open_admin():
    subprocess.Popen(["python", "admin.py"])

# Buttons
btn_style = {"width": 25, "pady": 8, "bg": "#57a1f8", "fg": "white", "font": ("Segoe UI", 11)}

tk.Button(root, text="📧 Compose Email", command=open_compose, **btn_style).pack(pady=10)
tk.Button(root, text="📂 View Inbox", command=open_inbox, **btn_style).pack(pady=10)
tk.Button(root, text="🛠 Admin Panel", command=open_admin, **btn_style).pack(pady=10)

# Run event loop
root.mainloop()