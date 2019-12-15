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
import hashlib

import peach_model as pModel

from PyQt5.QtMultimedia import QMediaPlaylist, QMediaContent, QMediaPlayer

class peachData:
    def __init__(self):
        self.path = "\\".join(sys.argv[0].split("\\")[:-1])
        self.billBoardChart= pModel.billboardChart()
        self.soundseaChart = pModel.soundseaChart()
        self.directoryMusicDict = dict()
        self.conn = sqlite3.connect('music_database.db')
        self.c = self.conn.cursor()

    def setPath(self, path):
        self.path = path

    def getPath(self):
        return self.path
    
    def initChart(self):
        self.billBoardChart.initBillboardChart()
        self.soundseaChart.initSoundseaChart()
    
    def initChartDict(self):
        self.billBoardChart.initBillboardChartDict()
        self.soundseaChart.initSoundseaChartDict()

    def getBillboardChartDict(self):
        return self.billBoardChart.getBillboardChartDict()

    def getSoundseaChartDict(self):
        return self.soundseaChart.getSoundseaChartDict()

    def initDirectory(self):
        pass

    def getDirectoryMusicDict(self):
        return self.directoryMusicDict
        
    def downloadMusic(self ,artist, song):
        downloader = pModel.peachTube(self.path, artist,song,self.directoryMusicDict)
        h = hashlib.sha1()
        h.update((song +" "+artist).encode('utf-8'))
        filename =  h.hexdigest() + ".mp3"
        self.c.execute('''INSERT INTO directory_music (song_name ,artist_name,file_name, created_at) VALUES (?,?,?,DATETIME(\'NOW\'));''',(str(song),str(artist),str(filename)))
        downloader.start()

class musicPlayer:
    def __init__(self, parent):
        # 윈도우 객체
        self.parent = parent
        self.player = QMediaPlayer()
        self.player.currentMediaChanged.connect(self.mediaChanged)
        self.player.durationChanged.connect(self.durationChanged)
        self.player.positionChanged.connect(self.positionChanged)
         
        self.playlist = QMediaPlaylist()

    def getPlayer(self):
        return self.player

    def play(self, playlists, startRow=0, option=QMediaPlaylist.Sequential):       
        if self.player.state() == QMediaPlayer.PausedState:
            self.player.play()
        else:              
            self.createPlaylist(playlists, startRow, option)            
            self.player.setPlaylist(self.playlist)
            self.playlist.setCurrentIndex(startRow)
            self.player.play()          
         
    def pause(self):
        self.player.pause()         
 
    def stop(self):
        self.player.stop()
 
    def prev(self):        
        self.playlist.previous()     
 
    def next(self):
        self.playlist.next()
 
    def createPlaylist(self, playlists, startRow=0, option=QMediaPlaylist.Sequential):        
        self.playlist.clear()      
 
        for path in playlists:
            url = QUrl.fromLocalFile(path)
            self.playlist.addMedia(QMediaContent(url))
 
        self.playlist.setPlaybackMode(option)
 
    def updatePlayMode(self, option):
        self.playlist.setPlaybackMode(option)
 
    def upateVolume(self, vol):
        self.player.setVolume(vol)
 
    def mediaChanged(self, e):
        self.parent.updateMediaChanged(self.playlist.currentIndex())       
 
    def durationChanged(self, msec):
        if msec>0:
            self.parent.updateDurationChanged(self.playlist.currentIndex(), msec)
 
    def positionChanged(self, msec):
        if msec>0:
            self.parent.updatePositionChanged(self.playlist.currentIndex(), msec)


# 선수
# 디렉토리 모델부분에서 DB 수정 하는 코드

# initDirectory에서
# 컨트롤러에서 DB랑, 그 디렉토리 파일 목록 받아들여서
# 서로 대응시키기
# 대응이 안되는 경우가 있다면 
# DB에서 삭제하고 디렉토리에 반영하지 않음.

