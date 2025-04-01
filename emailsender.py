import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os
import schedule
import time
import pyttsx3
from dotenv import load_dotenv

# Get credentials from environment variables
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PSWD = os.getenv("EMAIL_PSWD")

def send_emails():
    # Read data from Excel
    df = pd.read_excel(r"D:\mail_list1.xlsx")

    # Check if all required columns exist in DataFrame
    required_columns = ['Name', 'Email', 'Subject', 'Body', 'Attachments']
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns: 
        print(f"Error: Missing column(s) in the Excel file: {', '.join(missing_columns)}")
        return

    # Iterate over rows
    for index, row in df.iterrows():
        # Extract email and other relevant data
        email = row['Email']
        name = row['Name']
        subject = row['Subject']
        body = row['Body']
        attachment_files = str(row['Attachments']).strip().split(';')

        # Construct the email
        msg = MIMEMultipart()
        msg['From'] = 'EMAIL_USER'
        msg['To'] = email
        msg['Subject'] = subject

        body_text = f'Hello {name},\n\n{body}'
        msg.attach(MIMEText(body_text, 'plain'))

        # Add attachments to the email if they exist
        for attachment_filename in attachment_files:
            attachment_filename = attachment_filename.strip()
            if attachment_filename and os.path.exists(attachment_filename):
                with open(attachment_filename, "rb") as attachment_file:
                    part = MIMEApplication(attachment_file.read(), Name=os.path.basename(attachment_filename))
                part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment_filename)}"'
                msg.attach(part)

        # Send the email with attachment
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login('EMAIL_USER', 'EMAIL_PSWD')
            server.send_message(msg)
            server.quit()
            
            say_message(f"Email sent to {email} successfully.")
        except Exception as e:
            # Silently handle the exception without printing
            pass

def say_message(message):
    # Initialize the TTS engine
    engine = pyttsx3.init()
    
    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech (words per minute)
    engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)

    # Say the message
    engine.say(message)
    
    # Wait for speech to complete
    engine.runAndWait()
    print(message)

say_message("WELCOME TO PYMAIL!")  
print(" ")
say_message("Enter How Many times email to be sent:")  
times = int(input())  # variable for times.
say_message('Enter the time period (in sec):')
interval = int(input())  # variable for interval.
say_message('Enter the time (in format HH:MM):')             
Time = str(input())  # variable for clock time.
print(" ")

# Function to resend emails at a fixed interval
def resend_email_fixed_interval(interval, times):
    for i in range(times):
        send_emails()
        say_message(f"-----Email is sent {i+1} times successfully.-----")
        print(" ")
        time.sleep(interval)
    say_message(f"-----------------------------Email is sent {times} times successfully.----------------------------")
    print(" ")
    return True  # Indicate that all emails have been sent

# Schedule email sending
schedule.every().day.at(Time).do(resend_email_fixed_interval, interval, times)

# Run the scheduler
success = False
while not success:  # Exit the loop when all emails have been sent
    success = schedule.run_pending()
    time.sleep(1)
