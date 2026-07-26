import sqlite3

conn = sqlite3.connect("club.db")
conn.execute(
    "DELETE FROM responses"
)
conn.commit()
conn.close()