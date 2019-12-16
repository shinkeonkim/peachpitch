import sqlite3
import billboard

conn = sqlite3.connect('music_database.db')
c = conn.cursor()
# chart_billboard
c.execute('''
CREATE TABLE chart_billboard (id INTEGER PRIMARY KEY NOT NULL, song_name TEXT, artist_name TEXT, created_at DATETIME)
''')
# chart_soundsea
c.execute('''
CREATE TABLE chart_soundsea (id INTEGER PRIMARY KEY NOT NULL, song_name TEXT, artist_name TEXT , created_at DATETIME)
''')
# directory_music
c.execute('''
CREATE TABLE directory_music (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, song_name TEXT, artist_name TEXT,file_name TEXT, created_at DATETIME)
''')

c.execute('''
CREATE TABLE SETTING (billboard_chart_updated_at DATETIME, soundsea_chart_updated_at DATETIME, path TEXT)
''')

c.execute('''
CREATE TABLE selected_music (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, song_name TEXT, artist_name TEXT,file_name TEXT, created_at DATETIME)
''')

conn.commit()