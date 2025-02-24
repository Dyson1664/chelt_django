import sqlite3

# Connect to your SQLite database
conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()

# List all tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in the database:")
for table in tables:
    print(table[0])

# For example, query all data from a specific table:
# cursor.execute("SELECT * FROM your_table_name;")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

conn.close()