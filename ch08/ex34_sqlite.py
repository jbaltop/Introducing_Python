# p261

import sqlite3

conn = sqlite3.connect("data/enterprise.db")
curs = conn.cursor()

curs.execute("SELECT * FROM zoo")
rows = curs.fetchall()
print(rows)

curs.execute("SELECT * FROM zoo ORDER BY count")
print(curs.fetchall())

curs.execute("SELECT * FROM zoo ORDER BY count DESC")
print(curs.fetchall())

curs.execute("SELECT * FROM zoo WHERE damages = (SELECT MAX(damages) FROM zoo)")
print(curs.fetchall())

curs.close()
conn.close()
