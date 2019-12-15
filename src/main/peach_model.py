import sqlite3
import billboard
import pytube
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import subprocess
import threading
import sys

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_argument('lang=ko_KR')

driver = webdriver.Chrome('C:/Users/kimshinkeon/Desktop/peachpitch/chromedriver.exe',chrome_options=options)
        
class billboardChart:
    def __init__(self):
        self.billboardCharDict = {}
        self.conn = sqlite3.connect('music_database.db')
        self.c = self.conn.cursor()

    def initBillboardChart(self):
        self.c.execute('''DELETE FROM chart_billboard''')
        
        chart = billboard.ChartData('hot-100')
        for i in range(100):
            self.billboardCharDict[i+1] = {"song": chart[i].title ,"artist": chart[i].artist}
            self.c.execute('''INSERT INTO chart_billboard VALUES (?,?,?,DATETIME(\'NOW\'));''',(i+1,chart[i].title,chart[i].artist))
        self.conn.commit()

    def initBillboardChartDict(self):
        self.c.execute("SELECT * FROM chart_billboard")
        all_rows = self.c.fetchall()
        ret = {}
        for i in all_rows:
            ret[i[0]] = {"song": i[1], "artist": i[2]}
        self.billboardCharDict = ret
        self.conn.commit()

    def getBillboardChartDict(self):
        return self.billboardCharDict

    def setUpatedAt(self):
        # 추후 구현
        pass

class soundseaChart:
    def __init__(self):
        self.soundseaChartDict = {}
        self.conn = sqlite3.connect('music_database.db')
        self.c = self.conn.cursor()
    
    def initSoundseaChart(self):
        ret = {}

        global driver
        link = 'http://www.soribada.com/music/chart/daily'
        driver.get(link)
        driver.implicitly_wait(10)
        html = driver.page_source

        #print(html)
        soup = BeautifulSoup(html, 'html.parser')

        try:
            songList = soup.select(
                '.music-list > .listen > .list-area-cont > div.list-area2 > span > span.song-title'
            )
            artistList = soup.select(
                '.music-list > .listen > .list-area-cont > div.list-area2 > span.link-type2-name'
            )
        except:
            print("sound sea music chart can't find!")
            return
        else:
            if len(songList) != len(artistList):
                print("crawling Error!")
                return
            
            for i in range(len(songList)):
                ret[i+1] = {"song":str(songList[i].text).strip() , "artist": str(artistList[i].text).strip()}
            
            self.c.execute('''DELETE FROM chart_soundsea''')
            self.soundseaChartDict = ret
            for i in range(1,len(ret)+1):
                self.c.execute('''INSERT INTO chart_soundsea VALUES (?,?,?,DATETIME(\'NOW\'));''',(str(i),ret[i]['song'],ret[i]['artist']))
        self.conn.commit()
    
    def initSoundseaChartDict(self):
        self.c.execute("SELECT * chart_soundsea")
        all_rows = self.c.fetchall()
        ret = {}
        for i in all_rows:
            ret[i[0]] = {"song": i[1], "artist": i[2]}
        self.billboardCharDict = ret
        self.conn.commit()
    
    def getSoundseaChartDict(self):
        return self.soundseaChartDict

    def setUpdatedAt(self):
        pass

class peachTube(threading.Thread):
    def __init__(self,directory_path,artist,title):
        threading.Thread.__init__(self)
        self.directory_path = directory_path
        self.artist = artist
        self.title = title

    def searchSong(self,parsingTag = 'h3 > a'):
        link = 'https://www.youtube.com/results?search_query='
        link = link + "'"+self.artist+"'"+ "+" + "'"+self.title+"'"
        req = requests.get(link)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')

        try:
            resultLink = soup.select(
                parsingTag
            )[0]['href']
            print("https://www.youtube.com/"+resultLink)
        except:
            print(link)
            return "Error"    
        return "https://www.youtube.com/"+resultLink

    def run(self):
        try:
            yt = pytube.YouTube(self.searchSong())
            parent_dir = self.directory_path+"/video/"
            parent_dir2 = self.directory_path+"/audio/"
            print(parent_dir,parent_dir2)
            vids = yt.streams.filter(mime_type = "video/mp4").first()
            print("*")
            default_filename = vids.default_filename
            print("*")
            vids.download(parent_dir)
            print("*")
        except:
            print("Download Error")
        else:
            new_filename = str(default_filename).replace(".mp4",".mp3")
            subprocess.Popen(['ffmpeg', '-i', parent_dir + default_filename, parent_dir2 + new_filename])
            print("Download Complete!")


if __name__ == "__main__":
    # peacheTube
    pTube = peachTube("/".join(sys.argv[0].split("\\")[:-1]),"IU","love poem")
    pTube.start()
    
    # billboard
    test = billboardChart()
    test.initBillboardChart()
    print(test.getBillboardChartDict())
    
    # soundsea
    test = soundseaChart()
    test.initSoundseaChart()
    print(test.getSoundseaChartDict())