from tkinter import *
from tkinter import messagebox
import tkinter as tk
import smtplib
import imaplib
import email
from email.header import decode_header
import datetime

# Create the GUI
root = tk.Tk()
root.title("PyMail")

# Create the compose page
compose_frame = tk.Frame(root)
compose_frame.pack(side="top", fill="both", expand=True)

# Create the sender email entry
entry_sender_email = tk.Entry(compose_frame)
entry_sender_email.grid(row=0, column=0, padx=10, pady=10)

# Create the recipient email entry
entry_recipient_email = tk.Entry(compose_frame)
entry_recipient_email.grid(row=1, column=0, padx=10, pady=10)

# Create the subject entry
entry_subject = tk.Entry(compose_frame)
entry_subject.grid(row=2, column=0, padx=10, pady=10)

# Create the message text box
text_message = tk.Text(compose_frame, height=10, width=50)
text_message.grid(row=3, column=0, padx=10, pady=10)

# Function to send an email
def send_email():
    # Get the input values
    sender_email = entry_sender_email.get()
    recipient_email = entry_recipient_email.get()
    subject = entry_subject.get()
    message = text_message.get("1.0", "end-1c")

    # Validate the input values
    if not (sender_email and recipient_email and subject and message):
        messagebox.showerror("Error", "All fields are required.")
        return

    # Send the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, "your_password_here")
        message = f"Subject: {subject}\n\n{message}"
        server.sendmail(sender_email, recipient_email, message)
        server.quit()
        messagebox.showinfo("Success", "Email sent successfully!")

        # Display the email in the GUI
        listbox_emails.insert('end', f"Subject: {subject}\nFrom: {sender_email}\nTo: {recipient_email}\nDate: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n{message}\n")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the send button
button_send = tk.Button(compose_frame, text="Send", command=send_email)
button_send.grid(row=4, column=0, padx=10, pady=10)

# Create the email listbox
listbox_emails = tk.Listbox(root, height=10, width=50)
listbox_emails.pack(side="left", fill="both", expand=True)

# Create the scrollbar
scrollbar_emails = tk.Scrollbar(root)
scrollbar_emails.pack(side="right", fill="both")

# Configure the scrollbar for the listbox
listbox_emails.configure(yscrollcommand=scrollbar_emails.set)
scrollbar_emails.configure(command=listbox_emails.yview)

# Function to send an email
def send_email():
    # Get the input values
    sender_email = entry_sender_email.get()
    recipient_email = entry_recipient_email.get()
    subject = entry_subject.get()
    message = text_message.get("1.0", "end-1c")

    # Validate the input values
    if not (sender_email and recipient_email and subject and message):
        messagebox.showerror("Error", "All fields are required.")
        return

    # Send the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, "your_password_here")
        message = f"Subject: {subject}\n\n{message}"
        server.sendmail(sender_email, recipient_email, message)
        server.quit()
        messagebox.showinfo("Success", "Email sent successfully!")

        # Display the email in the GUI
        listbox_emails.insert('end', f"Subject: {subject}\nFrom: {sender_email}\nTo: {recipient_email}\nDate: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n{message}\n")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to retrieve and display the latest emails
def get_emails(email_address, password):
    # Connect to the email server
    try:
        server = imaplib.IMAP4_SSL('imap.gmail.com')
        server.login(email_address, password)

        # Select the email folder
        server.select('inbox')

        # Get the list of emails
        result, data = server.uid('search', None, "ALL")
        email_ids = data[0].split()

        # Clear the Listbox widget
        listbox_emails.delete(0, 'end')

        # Display the list of emails
        for email_id in email_ids:
            result, email_data = server.uid('fetch', email_id, '(BODY.PEEK[])')
            raw_email = email_data[0][1].decode('utf-8')
            email_message = email.message_from_string(raw_email)
            subject = decode_header(email_message['Subject'])[0][0]
            if isinstance(subject, bytes):
                subject = subject.decode('utf-8')
            from_email = decode_header(email_message['From'])[0][0]
            if isinstance(from_email, bytes):
                from_email = from_email.decode('utf-8')
            to_email = decode_header(email_message['To'])[0][0]
            if isinstance(to_email, bytes):
                to_email = to_email.decode('utf-8')
            date_sent = email_message['Date']
            listbox_emails.insert('end', f"Subject: {subject}\nFrom: {from_email}\nTo: {to_email}\nDate: {date_sent}\n")

        server.close()
        server.logout()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Get the latest emails
get_emails("your_email_address_here", "your_password_here")

# Start the main event loop
root.mainloop()