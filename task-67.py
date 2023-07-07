import sqlite3

conn = sqlite3.connect('database2.db', detect_types=sqlite3.PARSE_DECLTYPES)
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS books
(id INTEGER PRIMARY KEY, name TEXT, author TEXT, release DATE)''')

cursor.execute("INSERT INTO books (name, author, release) VALUES (?, ?, ?)",
               ('Книга 1', 'Д.В.Назаров', ' 2003-02-12'))
cursor.execute("INSERT INTO books (name, author, release) VALUES (?, ?, ?)",
               ('Книга 2', 'В.Ф.Назаров', '1888-02-15'))
cursor.execute("INSERT INTO books (name, author, release) VALUES (?, ?, ?)",
               ('Книга 3', 'А.А.Назаров', '1999-07-07'))

cursor.execute("SELECT * FROM books WHERE DATE(release) > '2000-01-01'")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.commit()
conn.close()