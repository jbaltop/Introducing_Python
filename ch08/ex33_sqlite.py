# p260

import sqlite3

conn = sqlite3.connect("output/enterprise.db")
curs = conn.cursor()

curs.execute('INSERT INTO zoo VALUES("duck", 5, 0.0)')
curs.execute('INSERT INTO zoo VALUES("bear", 2, 1000.0)')

ins = "INSERT INTO zoo (critter, count, damages) VALUES(?, ?, ?)"
curs.execute(ins, ("weasel", 1, 2000.0))

conn.commit()

curs.close()
conn.close()
