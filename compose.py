from tkinter import *
from tkinter import messagebox
import smtplib
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

# Fetch all recipient emails from the 'users' table
def fetch_all_emails():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("HOST"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            database=os.getenv("DATABASE")
        )
        cursor = conn.cursor()
        cursor.execute("SELECT email FROM users")
        results = cursor.fetchall()
        return [email[0] for email in results]
    except Exception as e:
        messagebox.showerror("Error", f"DB error: {e}")
        return []

# Send to specified comma-separated emails
def send_email():
    sender = entry_sender.get()
    recipient_raw = entry_recipient.get()
    subject = entry_subject.get()
    message_body = text_message.get("1.0", "end-1c")

    if not (sender and recipient_raw and subject and message_body):
        messagebox.showerror("Error", "All fields are required.")
        return

    recipients = [email.strip() for email in recipient_raw.split(",") if email.strip()]

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        password = os.getenv("EMAIL_PASS")
        server.login(sender, password)

        msg = f"Subject: {subject}\n\n{message_body}"
        server.sendmail(sender, recipients, msg)
        server.quit()
        messagebox.showinfo("Success", f"Email sent to {len(recipients)} recipient(s)!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Send to all contacts pulled from the database
def send_to_all():
    sender = entry_sender.get()
    subject = entry_subject.get()
    message_body = text_message.get("1.0", "end-1c")

    if not (sender and subject and message_body):
        messagebox.showerror("Error", "From, Subject, and Message are required.")
        return

    recipients = fetch_all_emails()
    if not recipients:
        return

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        password = os.getenv("EMAIL_PASS")
        server.login(sender, password)

        msg = f"Subject: {subject}\n\n{message_body}"
        server.sendmail(sender, recipients, msg)
        server.quit()
        messagebox.showinfo("Success", f"Email sent to {len(recipients)} contact(s)!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# UI setup
root = Tk()
root.title("Compose Email")
root.geometry("500x460")
root.configure(bg="white")

Label(root, text="From:", bg="white").pack(pady=(10, 0))
entry_sender = Entry(root, width=50)
entry_sender.pack()

Label(root, text="To (comma-separated):", bg="white").pack(pady=(10, 0))
entry_recipient = Entry(root, width=50)
entry_recipient.pack()

Label(root, text="Subject:", bg="white").pack(pady=(10, 0))
entry_subject = Entry(root, width=50)
entry_subject.pack()

Label(root, text="Message:", bg="white").pack(pady=(10, 0))
text_message = Text(root, height=10, width=60)
text_message.pack()

Button(root, text="Send", command=send_email, bg="#57a1f8", fg="white").pack(pady=5)
Button(root, text="Send to All Contacts", command=send_to_all, bg="#28a745", fg="white").pack(pady=5)

root.mainloop()