import sqlite3

conn = sqlite3.connect("club.db")
conn.executescript(open("schema.sql").read())
conn.close()