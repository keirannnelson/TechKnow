import sqlite3

conn = sqlite3.connect("leetcode.db")
cursor = conn.cursor()

for row in cursor.execute("SELECT title, difficulty, success_rate FROM questions LIMIT 10"):
    print(f"{row[0]} is {row[1]} with a {row[2]}% acceptance")

conn.close()