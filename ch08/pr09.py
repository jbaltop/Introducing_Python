# p285

import sqlite3

conn = sqlite3.connect("data/books.db")
curs = conn.cursor()

curs.execute("SELECT * FROM books ORDER BY year")
print(curs.fetchall())

curs.close()
conn.close()
