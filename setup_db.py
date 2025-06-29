import mysql.connector

# Connect to MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin@123",  # Ensure this matches your .env file
)
cursor = conn.cursor()

# Create the database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS USER")
cursor.execute("USE USER")

# Create the signup table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS signup (
        id INT AUTO_INCREMENT PRIMARY KEY,
        email VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL
    )
""")

# Insert some dummy users
dummy_users = [
    ("john.doe@gmail.com", "pass123"),
    ("jane.smith@yahoo.com", "welcome456"),
    ("sahil.dev@pmail.com", "secure789")
]

cursor.executemany("INSERT INTO signup (email, password) VALUES (%s, %s)", dummy_users)
conn.commit()

print("✅ Database setup complete with dummy data.")
cursor.close()
conn.close()