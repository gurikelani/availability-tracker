import sqlite3

conn = sqlite3.connect("club.db")

conn.execute(
    "INSERT INTO fixtures (opponent, date, location) VALUES (?, ?, ?)",
    ("UCL 2nd XI", "2026-09-14", "Honor Oak Park"),
)
conn.commit()

rows = conn.execute("SELECT * FROM fixtures").fetchall()
print(rows)

conn.close()