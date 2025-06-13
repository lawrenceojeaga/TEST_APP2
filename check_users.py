import sqlite3

# Path to your DB file
conn = sqlite3.connect("instance/products.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM user")
rows = cursor.fetchall()

# Print the users
for row in rows:
    print(row)

conn.close()