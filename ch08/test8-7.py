import csv
import sqlite3

with open("books2.csv", "rt", encoding="utf-8") as fin:
    cin = csv.DictReader(fin)
    books = [row for row in cin]

conn = sqlite3.connect("books.db")
curs = conn.cursor()
ins = "INSERT INTO books (title, author, year) VALUES(?, ?, ?)"

for book in books:
    curs.execute(ins, (book["title"], book["author"], book["year"]))

conn.commit()  # You have to commit before closing a DB file

curs.close()
conn.close()
