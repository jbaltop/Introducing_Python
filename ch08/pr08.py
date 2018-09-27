# p285

import sqlite3

conn = sqlite3.connect("data/books.db")
curs = conn.cursor()

curs.execute("SELECT title FROM books ORDER BY title")
print(curs.fetchall())

curs.close()
conn.close()
