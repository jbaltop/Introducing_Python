# p260

import sqlite3

conn = sqlite3.connect("output/enterprise.db")
curs = conn.cursor()

print(
    curs.execute(
        "CREATE TABLE zoo (critter VARCHAR(20) PRIMARY KEY, count INT, damages FLOAT)"
    )
)

curs.close()
conn.close()
