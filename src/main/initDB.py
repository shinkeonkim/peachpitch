import sqlite3
import billboard

conn = sqlite3.connect('music_database.db')
c = conn.cursor()
"""
c.execute('''
CREATE TABLE chart_billboard (id INTEGER PRIMARY_KEY NOT NULL, title TEXT, artist TEXT, youtube_link TEXT, created_at DATETIME)
''')

c.execute('''
CREATE TABLE SETTING (id INTEGER PRIMARYKEY NOT NULL, name TEXT, value TEXT, created_at DATETIME, updated_at DATETIME)
''')

"""