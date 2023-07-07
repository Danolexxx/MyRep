import sqlite3

conn = sqlite3.connect('database_films.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS films
(id INTEGER PRIMARY KEY, name TEXT, genre TEXT, rating REAL)''')

cursor.execute("INSERT INTO films (name, genre, rating) VALUES (?, ?, ?)", ('Достать ножи', 'детектив', 8))
cursor.execute("INSERT INTO films (name, genre, rating) VALUES (?, ?, ?)", ('Маяковский', 'автобиография', 8.2))

cursor.execute("SELECT * FROM films WHERE genre = 'детектив'")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.commit()
conn.close()
