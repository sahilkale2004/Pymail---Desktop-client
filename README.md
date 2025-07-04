📬 PyMail – Desktop Email Client in Python

PyMail is a lightweight, GUI-based email client built with Python’s Tkinter library. It lets you compose, send, and manage emails securely, with support for sending messages to individual users or everyone in your MySQL-stored contact list—making it ideal for team-wide announcements or personal productivity.

🚀 Features

- ✅ Compose and send emails via Gmail SMTP  
- ✅ Send to one or multiple addresses  
- ✅ One-click **Send to All Contacts** from MySQL  
- ✅ Environment variable protection with `.env`  
- ✅ Polished desktop UI with Tkinter  
- ✅ Modular architecture: compose, inbox, admin panel  

---

## 🛠 Tech Stack

- Python 3
- Tkinter (UI)
- smtplib / imaplib (email handling)
- mysql-connector-python (database interaction)
- dotenv (secure configuration)

---

## 📦 Installation & Usage

1. **Clone this repo:**

   ```bash
   git clone https://github.com/sahilkale2004/PyMail.git
   cd PyMail
   ```

2. **Set up your `.env` file:**

   ```
   HOST=localhost
   USER=your_mysql_username
   PASSWORD=your_mysql_password
   DATABASE=your_database_name
   EMAIL_PASS=your_gmail_app_password
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the app:**

   ```bash
   python Loginpage.py
   ```

5. Log in with a user account → access the dashboard → start sending!

---

## 🧠 Future Plans

- Add rich text / HTML email support  
- Filter or segment recipients by role or tags  
- Log sent emails and add delivery status feedback  
- Deploy backend services with Flask or Django  
- Cross-platform build (Windows / Mac) with `PyInstaller`

---

## 🙋‍♂️ Author

Built by [Sahil Kale](https://github.com/sahilkale2004) — a passionate Python developer exploring full-stack solutions with a creative twist ✨
