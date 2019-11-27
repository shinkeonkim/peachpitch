import sqlite3

conn = sqlite3.connect('music_database.db')
c = conn.cursor()

for i in c.execute('''SELECT * FROM chart_billboard ORDER BY id'''):
    print(i)