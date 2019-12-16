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
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QMediaPlaylist, QMediaContent, QMediaPlayer

import peach_model as pModel


class peachData:
    def __init__(self):
        self.path = "\\".join(sys.argv[0].split("\\")[:-1])
        self.billBoardChart= pModel.billboardChart()
        self.soundseaChart = pModel.soundseaChart()
        self.selectedMusic = pModel.selectedMusicDict()
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
        self.selectedMusic.initSelectedMusicDict()

    def initChartDict(self):
        self.billBoardChart.initBillboardChartDict()
        self.soundseaChart.initSoundseaChartDict()
        self.selectedMusic.initSelectedMusicDict()

    def getBillboardChartDict(self):
        return self.billBoardChart.getBillboardChartDict()

    def getSoundseaChartDict(self):
        return self.soundseaChart.getSoundseaChartDict()

    def getSelectedMusicDict(self):
        return self.selectedMusic.getSelectedMusicDict()

    def getSelectedMusicPlaylist(self):
        D = self.selectedMusic.getSelectedMusicDict()
        #print(D)
        return [D[i]['filename'].replace("\\","/") for i in D]

    def updateSelectedMusicDict(self,music_dict):
        self.selectedMusic.addMusic(music_dict)

    def initDirectory(self):
        self.c.execute("SELECT * FROM directory_music")
        all_rows = self.c.fetchall()
        ret = {}
        for i in all_rows:
            ret[i[0]] = {"song": i[1],"artist": i[2], "filename": i[3]}
        self.directoryMusicDict = ret 
        self.conn.commit()

    def getDirectoryMusicDict(self):
        return self.directoryMusicDict
        
    def downloadMusic(self ,artist, song):
        downloader = pModel.peachTube(self.path, artist,song)    
        h = hashlib.sha1()
        h.update((song +" "+artist).encode('utf-8'))
        filename =  h.hexdigest() + ".mp3"
        self.c.execute('''INSERT INTO directory_music (song_name, artist_name, file_name, created_at) VALUES (?,?,?,DATETIME(\'NOW\'));''',(str(song),str(artist),str(filename)))
        
        self.conn.commit()
        downloader.start()

class musicPlayer:
    def __init__(self, parent):
        # 윈도우 객체
        self.parent = parent
        self.player = QMediaPlayer()
        self.player.currentMediaChanged.connect(self.mediaChanged)
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
 
    def updateVolume(self, vol):
        self.player.setVolume(vol)
 
    def mediaChanged(self, e):
        self.parent.updateMediaChanged(self.playlist.currentIndex())