import sqlite3
import billboard

conn = sqlite3.connect('music_database.db')
c = conn.cursor()
"""
c.execute('''
CREATE TABLE chart_billboard (id INTEGER PRIMARY_KEY NOT NULL, title TEXT, artist TEXT, youtube_link TEXT, created_at DATETIME)
''')
"""
# chart들
l = billboard.charts()

#hot-100 chart 가져오기
s = billboard.ChartData('hot-100')

chart_list = []
for i in range(100):
    chart_list.append((s[i].title,s[i].artist))

#print(chart_list)

c.execute('''DELETE FROM chart_billboard''')

cnt = 0
for i in chart_list:
    cnt+=1
    c.execute('''INSERT INTO chart_billboard VALUES (?,?,?,?,DATETIME(\'NOW\'));''',(cnt,i[0],i[1],""))

# Save (commit) the changes
conn.commit()
conn.close()