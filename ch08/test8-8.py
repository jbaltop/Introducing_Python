import sqlite3

conn = sqlite3.connect('books.db')
curs = conn.cursor()
curs.execute('SELECT * FROM books ORDER BY title')
print(curs.fetchall())

curs.close()
conn.close()
