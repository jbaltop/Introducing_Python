# p285

import sqlalchemy

conn = sqlalchemy.create_engine("sqlite:///data/books.db")

rows = conn.execute("SELECT title FROM books ORDER BY title").fetchall()

for row in rows:
    print(row)
