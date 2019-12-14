import sqlite3
import billboard
import pytube
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import subprocess
import threading

class PeachData:

    def __init__(self):
        self._billboardMusicList = []
        self._soundseaMusicList = []

        self.conn = sqlite3.connect('music_database.db')
        self.c = self.conn.cursor()

    def initBillboard(self):
        l = billboard.charts()
        #hot-100 chart 가져오기
        s = billboard.ChartData('hot-100')

        chart_list = []
        for i in range(100):
            chart_list.append((s[i].title,s[i].artist,self.crawlingYoutube(s[i].artist,s[i].title, 'h3 > a')))
        #print(chart_list)

        self.c.execute('''DELETE FROM chart_billboard''')

        cnt = 0
        for i in chart_list:
            cnt+=1
            self.c.execute('''INSERT INTO chart_billboard VALUES (?,?,?,?,DATETIME(\'NOW\'));''',(cnt,i[0],i[1],i[2]))

        # Save (commit) the changes
        self.conn.commit()

    def setBillboardMusicList(self):
        ret = []
        self.c.execute("SELECT * FROM chart_billboard")
        all_rows = self.c.fetchall()
        for i in all_rows:
            ret.append(i)
        self._billboardMusicList = ret

    def getBillboardMusicList(self):
        return self._billboardMusicList

    def crawlingYoutube(self, artist, title,  parsingTag):
        link = 'https://www.youtube.com/results?search_query='
        link = link + "'"+artist+"'"+ "+" + "'"+title+"'"
        req = requests.get(link)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')

        try:
            resultLink = soup.select(
                parsingTag
            )[0]['href']
        except:
            print(link)
            return "Error"    
        return "https://www.youtube.com/"+resultLink

    def crawlingSoundSea(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")
        options.add_argument('lang=ko_KR')

        driver = webdriver.Chrome('C:/Users/kimshinkeon/Desktop/peachpitch/chromedriver.exe',chrome_options=options)
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
            return []
        else:
            #print(len(songList),len(artistList))
            
            if len(songList) != len(artistList):
                print("crawling Error!")
                return []
            
            ret = []
            for i in range(len(songList)):
                ret.append([str(songList[i].text).strip(),str(artistList[i].text).strip()])
            return ret

    def setSoundseaMusicList(self):
        self._soundseaMusicList = self.crawlingSoundSea()

    def getSoundseaMusicList(self):
        return self._soundseaMusicList

    def __del__(self):
        self.conn.commit()
        self.conn.close()

class YoutubeDownloader(threading.Thread):
    def __init__(self,link,directory):
        threading.Thread.__init__(self)
        self.link = link
        self.directory = directory
        
    def run(self):
        try:
            yt = pytube.YouTube(self.link)
            parent_dir = self.directory+"video/"
            parent_dir2 = self.directory+"audio/"

            vids = yt.streams.filter(mime_type = "video/mp4").first()

            default_filename = vids.default_filename
            vids.download(parent_dir)

        except:
            print("Download Error")
        else:
            new_filename = str(default_filename).replace(".mp4",".mp3")
            subprocess.Popen(['ffmpeg', '-i', parent_dir + default_filename, parent_dir2 + new_filename])
            print("Download Complete!")
