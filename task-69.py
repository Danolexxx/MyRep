import sqlite3

conn = sqlite3.connect('database_employees.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS employees
(id INTEGER PRIMARY KEY, name TEXT, function TEXT, salary REAL)''')

cursor.execute("INSERT INTO employees (name, function, salary) VALUES (?, ?, ?)",
               ('Грут', 'директор', 2000))
cursor.execute("INSERT INTO employees (name, function, salary) VALUES (?, ?, ?)",
               ('Жанна', 'менеджер', 900))
cursor.execute("INSERT INTO employees (name, function, salary) VALUES (?, ?, ?)",
               ('Элен', 'кассир', 1500))

cursor.execute("SELECT * FROM employees WHERE function = 'директор'")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.commit()
conn.close()