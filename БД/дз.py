import sqlite3

spis_1 = [10, 'world', 25, 12, 'python', 3, 'homework']

conn = sqlite3.connect('tab_hw.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT) ''')
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_2(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER) ''')
conn.commit()

for i in spis_1:
    if type(i) == str:
        a = i
        cursor.execute('''INSERT INTO tab_1(col_1) VALUES (?) ''', (a,))
        conn.commit()
        b = len(i)
        cursor.execute('''INSERT INTO tab_2(col_1) VALUES (?) ''', (b,))
        conn.commit()
    if type(i) == int:
        if i % 2 == 0:
            b = i
            cursor.execute('''INSERT INTO tab_2(col_1) VALUES (?) ''', (b,))
            conn.commit()
        else:
            a = 'нечётное'
            cursor.execute('''INSERT INTO tab_1(col_1) VALUES (?) ''', (a,))
            conn.commit()

cursor.execute('''SELECT id FROM tab_2''')
k = cursor.fetchall()
for i in k:
    for j in i:
        if j > 5:
            cursor.execute('''DELETE FROM tab_1 WHERE id = 1''')
            conn.commit()
        else:
            cursor.execute('''UPDATE tab_1 SET col_1 = "hello" WHERE id = 1''')
            conn.commit()
cursor.execute('''SELECT * FROM tab_1''')
h = cursor.fetchall()
cursor.execute('''SELECT * FROM tab_2''')
l = cursor.fetchall()
print(h)
print(l)









