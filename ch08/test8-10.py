import sqlalchemy

conn = sqlalchemy.create_engine("sqlite:///books.db")
rows = conn.execute("SELECT * FROM books ORDER BY title").fetchall()

for row in rows:
    print(row)
