import sqlite3
conn = sqlite3.connect("database.db")

print("Connected")

cmd = "CREATE TABLE reserved (name TEXT, arriving DATE, departing DATE)"

conn.execute(cmd)

print("Success!")

conn.close()