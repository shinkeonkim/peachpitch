import sqlite3
import billboard
import pytube

class PeachData:

    def __init__(self):
        self.billboardMusicList = []
        self.conn = sqlite3.connect('music_database.db')
        self.c = self.conn.cursor()
        self.initBillboard()
        self.setBillboardMusicList()

    def initBillboard(self):
        l = billboard.charts()
        #hot-100 chart 가져오기
        s = billboard.ChartData('hot-100')

        chart_list = []
        for i in range(100):
            chart_list.append((s[i].title,s[i].artist))

        #print(chart_list)

        self.c.execute('''DELETE FROM chart_billboard''')

        cnt = 0
        for i in chart_list:
            cnt+=1
            self.c.execute('''INSERT INTO chart_billboard VALUES (?,?,?,?,DATETIME(\'NOW\'));''',(cnt,i[0],i[1],""))

        # Save (commit) the changes
        self.conn.commit()

    def setBillboardMusicList(self):
        ret = []
        self.c.execute("SELECT * FROM chart_billboard")
        all_rows = self.c.fetchall()
        for i in all_rows:
            ret.append(i)
        self.billboardMusicList = ret

    def getBillboardMusicList(self):
        return self.billboardMusicList

    def __del__(self):
        self.conn.commit()
        self.conn.close()