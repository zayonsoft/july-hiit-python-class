import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    id = row[0]
    name = row[1]
    print(f"Id: {id}, name: {name}")

cursor.execute("DELETE FROM users WHERE id=1 or id=2;")
cursor.close()
conn.close()
