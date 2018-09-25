#!/usr/local/bin/python3

import sqlite3

conn = sqlite3.connect('books.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE books (title TEXT, author TEXT, year INT)''')
conn.commit()

curs.close()
conn.close()
