from tkinter import *
from tkinter import messagebox
import imaplib
import email
from email.header import decode_header
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_inbox():
    try:
        server = imaplib.IMAP4_SSL("imap.gmail.com")
        email_address = os.getenv("EMAIL_USER")
        password = os.getenv("EMAIL_PASS")
        server.login(email_address, password)
        server.select("inbox")

        status, messages = server.search(None, "ALL")
        mail_ids = messages[0].split()[-10:]  # Last 10 emails

        listbox.delete(0, END)

        for uid in reversed(mail_ids):
            status, msg_data = server.fetch(uid, "(RFC822)")
            raw_email = msg_data[0][1]
            email_msg = email.message_from_bytes(raw_email)

            subject, _ = decode_header(email_msg["Subject"])[0]
            subject = subject.decode() if isinstance(subject, bytes) else subject

            from_ = email_msg["From"]

            listbox.insert(END, f"From: {from_}")
            listbox.insert(END, f"Subject: {subject}")
            listbox.insert(END, "-" * 50)

        server.close()
        server.logout()
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = Tk()
root.title("Inbox")
root.geometry("600x400")

Button(root, text="Refresh Inbox", command=fetch_inbox, bg="#57a1f8", fg="white").pack(pady=5)

listbox = Listbox(root, width=80, height=20)
listbox.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar = Scrollbar(root, orient=VERTICAL, command=listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)
listbox.config(yscrollcommand=scrollbar.set)

fetch_inbox()
root.mainloop()