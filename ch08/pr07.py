# p285

import csv
import sqlite3

with open("data/books2.csv", "rt", encoding="utf-8") as fin:
    cin = csv.DictReader(fin)
    books = [row for row in cin]

conn = sqlite3.connect("output/books.db")
curs = conn.cursor()

ins = "INSERT INTO books (title, author, year) VALUES(?, ?, ?)"

for book in books:
    curs.execute(ins, (book["title"], book["author"], book["year"]))

conn.commit()

curs.close()
conn.close()
