#!/usr/local/bin/python3

import sqlite3

conn = sqlite3.connect('enterprise.db')
curs = conn.cursor()
curs.execute('INSERT INTO zoo VALUES("duck", 5, 0.0)')
curs.execute('INSERT INTO zoo VALUES("bear", 2, 1000.0)')
ins = 'INSERT INTO zoo (critter, count, damages) VALUES(?, ?, ?)'
curs.execute(ins, ('weasel', 1, 2000.0))
curs.execute('SELECT * FROM zoo')
rows = curs.fetchall()
print(rows)
curs.execute('SELECT * FROM zoo ORDER BY count')
print(curs.fetchall())
curs.execute('''SELECT * FROM zoo WHERE damages = (SELECT MAX(damages) FROM zoo)''')
print(curs.fetchall())

curs.close()
conn.close()
