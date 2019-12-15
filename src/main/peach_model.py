import sqlite3
import billboard
import pytube
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import subprocess
import threading

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
        pass

if __name__ == "__main__":
    test = billboardChart()
    test.initBillboardChartDict()
    print(test.getBillboardChartDict())
