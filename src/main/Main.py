import sys
import sip
import copy
import hashlib
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import QAudioProbe, QMediaPlayer, QMediaPlaylist, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget

import peach_controller as pcontroller

pData = pcontroller.peachData()
billboardChartDict = {}
soundseaChartDict = {}
directoryMusicDict = {}
selectedMusicDict = {}
playlist = []

class Window(QWidget):
    def __init__(self):
        super().__init__()
        
        global pData
        global playlist
        global billboardChartDict
        global soundseaChartDict
        global directoryMusicDict
        global selectedMusicDict
        # 추후 구현 db 갱신일 비교해서 최근이면 initChartDict()
        #pData.initChart()
        pData.initChartDict()
        pData.initDirectory()
        billboardChartDict = pData.getBillboardChartDict()
        soundseaChartDict = pData.getSoundseaChartDict()
        directoryMusicDict = pData.getDirectoryMusicDict()
        selectedMusicDict = pData.getSelectedMusicDict()
        
        playlist = pData.getSelectedMusicPlaylist()
        self.player = pcontroller.musicPlayer(self)
        self.selectedList = [0]
        self.playOption = QMediaPlaylist.Sequential
        self.createPlaylist
        self.cnt = 0
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.initVariable()
        self.initUI()

    def initVariable(self):
        self.imageDir = "../../img/"
        self.isExpanded = False


    def initUI(self):
        self.setGeometry(100,100,1200,500)
        self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setStyleSheet("* {background: qlineargradient(spread:pad, x1:0 y1:0, x2:1 y2:0, stop:0 #AA99FF, stop:1 #8BC6E8, stop:2 #99F4FF);"
        #                "color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 black);}");

        mainbox = QVBoxLayout()

        #타이틀바
        titlebox = QHBoxLayout()
        peachImage = QLabel(self)
        pixmap = QPixmap(self.imageDir+'peach.png')
        pixmap = pixmap.scaled(130, 130, Qt.KeepAspectRatio)
        peachImage.setPixmap(pixmap)
        peachImage.setStyleSheet('''
        background-color: #00ff0000;
        border-style: inset;
        border-width: 0px;
        border-radius: 10px;
        border-color: white;
        ''')
        minimizeButton = QPushButton("―")
        closeButton = QPushButton("X")
        minimizeButton.setFixedSize(25, 25)
        closeButton.setFixedSize(25, 25)
        minimizeButton.clicked.connect(lambda: self.showMinimized())
        minimizeButton.setStyleSheet('''
        background-color: #00ff0000;
        border-style: inset;
        border-width: 2px;
        border-radius: 10px;
        border-color: black;
        ''')
        closeButton.setStyleSheet('''
        background-color: #00ff0000;
        border-style: inset;
        border-width: 2px;
        border-radius: 10px;
        border-color: black;
        ''')
        closeButton.clicked.connect(QCoreApplication.instance().quit)
        
        titlebox.addWidget(peachImage)
        titlebox.addStretch(1)
        titlebox.addWidget(minimizeButton)
        titlebox.addWidget(closeButton)

        mainbox.addLayout(titlebox)
        
        #재생과 리스트를 구분지을 수 있는 vbox넣기 위한 self.hbox1
        self.hbox1 = QHBoxLayout()
        
        #이미지랑 재생 버튼 있는 vbox1
        vbox1 = QVBoxLayout()

        #이미지나 비주얼라이저 자리
        videoWidget = QVideoWidget()
        videoWidget.setFixedSize(800, 600)
        self.playButton = QPushButton()
        self.playButton.setFixedSize(20, 20)
        self.playButton.clicked.connect(self.play)
        self.mediaPlayer.setMedia(QMediaContent(QUrl(self.imageDir + 'peachvideo.avi')))

        self.mediaPlayer.setVideoOutput(videoWidget)

        #슬라이더
        playSlider = QSlider()
        playSlider.setOrientation(Qt.Horizontal)
        playSlider.setMinimum(0)
        playSlider.setMaximum(1000)
        playSlider.setValue(0)
        playSlider.setStyleSheet("""
        QSlider::groove:horizontal {
            background: white;
            height: 40px;
        }

        QSlider::sub-page:horizontal {
            background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,
                stop: 0 #66e, stop: 1 #bbf);
            background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,
                stop: 0 #bbf, stop: 1 #55f);
            height: 40px;
        }

        QSlider::add-page:horizontal {
            background: white;
            height: 40px;
        }

        QSlider::handle:horizontal {
            background: #55f;
            border: 0px;
            width: 13px;
            margin-top: 0px;
            margin-bottom: 0px;
            border-radius: 0px;
        }
        """)

        #동영상용 임시 버튼
        titlebox.addWidget(self.playButton)
        vbox1.addWidget(videoWidget)
        vbox1.addWidget(playSlider)
        
        #재생버튼들이랑 볼륨 설정 나눌 hbox2
        hbox2 = QHBoxLayout()

        #재생버튼들 나눌 hbox3
        hbox3 = QHBoxLayout()
        prevSongButton = QPushButton("｜◁")
        nextSongButton = QPushButton("▷｜")
        self.pausePlayButton = QPushButton("",self)
        self.pausePlayButton.setText("▶")
        
        prevSongButton.setStyleSheet('''
        background-color: #00ff0000;
        border-style: inset;
        border-width: 2px;
        border-radius: 10px;
        border-color: black;
        ''')
        nextSongButton.setStyleSheet('''
        background-color: #00ff0000;
        border-style: inset;
        border-width: 2px;
        border-radius: 10px;
        border-color: black;
        ''')
        self.pausePlayButton.setStyleSheet('''
        background-color: #00ff0000;
        border-style: inset;
        border-width: 2px;
        border-radius: 10px;
        border-color: black;
        ''')

        prevSongButton.setFixedSize(199, 110)
        nextSongButton.setFixedSize(199, 110)
        self.pausePlayButton.setFixedSize(199, 110)

        self.pausePlayButton.setCheckable(True)
        self.pausePlayButton.clicked.connect(self.changeImage)
        prevSongButton.clicked.connect(self.prev)
        nextSongButton.clicked.connect(self.next)

        hbox3.addStretch(1)
        hbox3.addWidget(prevSongButton)
        hbox3.addStretch(1)
        hbox3.addWidget(self.pausePlayButton)
        hbox3.addStretch(1)
        hbox3.addWidget(nextSongButton)
        hbox3.addStretch(1)

        hbox2.addLayout(hbox3)
        vbox1.addLayout(hbox2)

        #볼륨설정이랑 설정 버튼이 있는 hbox4
        hbox4 = QHBoxLayout()

        #볼륨설정 vbox2 hvolumeValue는 가운데에 숫자 넣기 위함
        vbox2 = QVBoxLayout()
        hvolumeValue = QHBoxLayout()

        self.volumeSlider = QDial()
        self.volumeSlider.setMinimum(0)
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setValue(40)
        self.volumeSlider.valueChanged.connect(self.sliderMoved)

        self.volumeValue = QLabel()
        self.volumeValue.setText(str(self.volumeSlider.value()))

        vbox2.addWidget(self.volumeSlider)
        hvolumeValue.addStretch(1)
        hvolumeValue.addWidget(self.volumeValue)
        hvolumeValue.addStretch(1)

        vbox2.addLayout(hvolumeValue)

        hbox4.addLayout(vbox2)
        hbox3.addLayout(hbox4)

        #설정버튼과 속도조절 vbox3
        vbox3 = QVBoxLayout()

        speedList = ["X 1.0", "X 0.25", "X 0.5", "X 0.75", "X 1.25", "X 1.5", "X 1.75", "X 2.0"]
        speedCombobox = QComboBox()
        speedCombobox.setFixedSize(80, 25)
        speedCombobox.setStyleSheet('''
        border: 2px solid black;
        selection-background-color: lightgray;
        ''')
        for i in speedList:
            speedCombobox.addItem(i)

        vbox3.addWidget(speedCombobox)

        #중간에 넣으려는 hbox5
        hbox5 = QHBoxLayout()
        settingButton = QPushButton()
        settingButton.setFixedSize(30, 30)
        settingButton.setStyleSheet('background-color: #00ff0000')
        settingButton.setIcon(QIcon(self.imageDir+'gear.png'))
        hbox5.addStretch(1)
        hbox5.addWidget(settingButton)
        hbox5.addStretch(1)
        vbox3.addLayout(hbox5)

        hbox3.addLayout(vbox3)

        #현재 재생목록 리스트 (hbox6)와 확장버튼 vbox4
        vbox4 = QVBoxLayout()
        hbox6 = QHBoxLayout()

        self.currentMusicList = QListWidget(self)
        self.currentMusicList.move(0,0)
        self.currentMusicList.setStyleSheet('''
        QListWidget{
        background-color: #00ff0000;
        border-style: inset;
        border-width: 2px;
        border-radius: 10px;
        border-color: black;
        }
        QListWidget::item {
        border: 0px solid red;
        }
        
        ''')

        hbox6.addWidget(self.currentMusicList)

        for i in selectedMusicDict:
            widget = QWidget()
            item = musicItem(selectedMusicDict[i]['song'],selectedMusicDict[i]['artist'],widget)
            #리스트에 위젯 넣기
            self.currentMusicList.addItem(item)
            self.currentMusicList.setItemWidget(item, widget)


        vbox4.addLayout(hbox6)

        #스페이스랑 확장버튼 삭제버튼 재생하기 버튼
        hbox7 = QHBoxLayout()

        deleteButton = QPushButton("""선택한 노래삭제""")
        deleteButton.setStyleSheet('''
        QPushButton {
        background-color: #00ff0000;
        border-style: inset;
        border-width: 2px;
        border-radius: 10px;
        border-color: black;
        }
        ''')
        deleteButton.setFixedSize(200,40)
        deleteButton.clicked.connect(self.listdelete)

        hbox7.addWidget(deleteButton)

        menuButton = QPushButton()
        menuButton.clicked.connect(self.expandWindow1)
        menuButton.setIcon(QIcon(self.imageDir+'plusbutton.png'))
        hbox7.addWidget(menuButton, alignment=Qt.AlignRight)
        vbox4.addLayout(hbox7)
        self.vbox5 = subWindow(billboardChartDict,soundseaChartDict,self.currentMusicList)

        self.hbox1.addLayout(vbox1)
        self.hbox1.addLayout(vbox4)
        mainbox.addLayout(self.hbox1)

        #메인 설정
        self.setLayout(mainbox)

    # 창을 옮긴다.
    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton and (event.globalY() - self.pos().y() <= 60):
            self.dragPos = event.globalPos()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and (event.globalY() - self.pos().y() <= 60):
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()


    def expandWindow1(self):
        if self.isExpanded:
            self.boxdelete(self.hbox1,self.vbox5)
            self.setGeometry(self.pos().x(), self.pos().y(), 1200, 500)
        else:
            self.setGeometry(self.pos().x(), self.pos().y(), 1568, 500)
            self.vbox5 = QVBoxLayout()
            self.expandWindow1 = subWindow(billboardChartDict,soundseaChartDict,self.currentMusicList)
            self.vbox5.addWidget(self.expandWindow1)
            self.hbox1.addLayout(self.vbox5)

        self.isExpanded = not self.isExpanded    

    
    def boxdelete(self, layout, box):
        for i in range(layout.count()):
            layout_item = layout.itemAt(i)
            if layout_item.layout() == box:
                self.deleteItemsOfLayout(layout_item.layout())
                layout.removeItem(layout_item)
                break

    def listdelete(self):
        try:
            #print(self.currentMusicList.currentItem().getSongName())
            for i in self.currentMusicList.selectedItems():
                self.currentMusicList.takeItem(self.currentMusicList.row(i))
        except:
            pass
    
    def itemClicked(self):
        L = self.sender
        youtubeDownload(L)

    def sliderMoved(self):
        self.volumeValue.setText(str(self.volumeSlider.value()))
        self.player.updateVolume(self.volumeSlider.value())

    def changeImage(self):
        self.cnt = (1- self.cnt)
        if self.cnt  == 1:
            if len(playlist) >0:
                self.player.play(playlist, self.selectedList[0], self.playOption)
        else:
            self.player.pause()
        
        self.pausePlayButton.setText({True: "❚❚", False: "▶"}[self.cnt])

    def selectChanged(self):
        self.selectedList.clear()        
        for item in self.currentMusicList.selectedItems():
            self.selectedList.append(item.row())
         
        self.selectedList = list(set(self.selectedList))
         
        if self.table.rowCount()!=0 and len(self.selectedList) == 0:
            self.selectedList.append(0)

        self.createPlaylist()
    
    def createPlaylist(self):
        playlist.clear()
        for i in range(self.currentMusicList.row()):
            artist = self.currentMusicList.itemFromIndex(i).getArtistName()
            title  = self.currentMusicList.itemFromIndex(i).getSongName()
            h = hashlib.sha1()
            h.update((title +" "+artist).encode('utf-8'))
            file =  h.hexdigest() + ".mp3"
            directory = pData.getPath()
            playlist.append((directory + "\\" + file).replace("\\\\","\\"))
        #print(playlist)
    
    def updateMediaChanged(self, index):
        if index>=0:
            self.currentMusicList.setCurrentRow(index)

    def deleteItemsOfLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)
                else:
                    self.deleteItemsOfLayout(item.layout())
    def prev(self):
        self.player.prev()
    
    def next(self):
        self.player.next()

    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.stop()
        else:
            self.mediaPlayer.play()

class subWindow(QWidget): 

    def __init__(self,billboardDict, soundseaDict, currentMusicList):
        super().__init__()
        global directoryMusicDict
        self.initVariable()
        self.billboardDict = billboardDict
        self.soundseaDict = soundseaDict
        self.currentMusicList = currentMusicList
        self.initUI()
        
    def initVariable(self):
        self.imageDir = "../../img/"

    def initUI(self):
        #확장 됬을때 self.vbox5
        self.vbox5 = QVBoxLayout()

        #탭뷰
        self.tabs = QTabWidget()
        self.myFileTab = QWidget()
        self.rankListTab = QWidget()

        self.myFileTab.setStyleSheet('''
        .QWidget {
        background-color: #f0f0f0 ;
        border-style: inset;
        border-width: 1px;
        border-radius: 10px;
        border-color: black;
        }
        ''')

        self.rankListTab.setStyleSheet('''
        .QWidget {
        background-color: #f0f0f0 ;
        border-style: inset;
        border-width: 1px;
        border-radius: 10px;
        border-color: black;
        }
        ''')

        self.tabs.addTab(self.myFileTab, "내 파일")
        self.tabs.addTab(self.rankListTab, "랭킹")
        self.tabs.setStyleSheet("""
        QTabBar::tab:selected { 
        background-color: black;
        font: bold;
        color: white; 
        }
        .QTabWidget {
        background-color: #f0f0f0 
        border-style: inset;
        border-width: 2px;
        border-radius: 10px;
        border-color: black;
        }
        
        """)

        #파일 탭뷰 안에서의 tvbox1 thbox1
        self.tvbox1 = QVBoxLayout()
        self.thbox1 = QHBoxLayout()

        self.refreshButton1 = QPushButton()
        self.refreshButton1.clicked.connect(self.refreshButton1Clicked)
        self.refreshButton1.setIcon(QIcon(self.imageDir+'refresh-button'))
        self.refreshButton1.setFixedSize(30,30)
        
        self.myFileSearchInput = QLineEdit()
        self.myFileSearchButton = QPushButton()
        self.myFileSearchButton.setFixedSize(30, 30)
        self.myFileSearchButton.setIcon(QIcon(self.imageDir + 'magnifying-glass.png'))

        self.thbox1.addStretch(5)
        self.thbox1.addWidget(self.myFileSearchInput)
        self.thbox1.addWidget(self.myFileSearchButton)
        self.thbox1.addStretch(2)
        self.thbox1.addWidget(self.refreshButton1)

        self.tvbox1.addLayout(self.thbox1)

        self.myFileList = QListWidget()
        self.myFileList.setStyleSheet("""
        .QListWidget {
        background-color: #f0f0f0;
        }
        QListWidget::item {
        background-color: rgb(255,255,255);
        }
        QListWidget::item:selected {
        background-color: rgb(128,128,255);
        }
        """)
        self.myFileList.itemDoubleClicked.connect(self.selectedListUpdate)

        self.tvbox1.addWidget(self.myFileList)

        self.myFileTab.setLayout(self.tvbox1)

        for i in directoryMusicDict:
            widget = QWidget()
            current = directoryMusicDict[i]
            item = musicItem(current['song'], current['artist'], widget)
            # 리스트에 위젯 넣기
            self.myFileList.addItem(item)
            self.myFileList.setItemWidget(item, widget)
        
        #랭킹 탭뷰 안에서의 tvbox2 thbox2
        self.tvbox2 = QVBoxLayout()
        self.thbox2 = QHBoxLayout()

        #랭킹 탭들
        self.rankTab = QTabWidget()
        self.rankTab.setStyleSheet("""
        QTabWidget::tab-bar { alignment: center; }
        """)
        billboardList = QListWidget()
        koreanRankList = QListWidget()

        billboardList.setStyleSheet("""
        QListWidget::item:selected {
        background: rgb(128,128,255);
        }
        """)
        koreanRankList.setStyleSheet("""
        QListWidget::item:selected {
        background: rgb(128,128,255);
        }
        """)


        self.reFreshButton2 = QPushButton()
        self.reFreshButton2.setIcon(QIcon(self.imageDir + 'refresh-button'))
        self.reFreshButton2.setFixedSize(30, 30)

        self.thbox2.addWidget(self.reFreshButton2, alignment=Qt.AlignRight)

        self.tvbox2.addLayout(self.thbox2)
        self.tvbox2.addWidget(self.rankTab)

        self.rankListTab.setLayout(self.tvbox2)

        self.vbox5.addWidget(self.tabs)
        self.rankTab.addTab(billboardList, "빌보드")
        self.rankTab.addTab(koreanRankList, "한국")
        

        for i in range(1,101):
            widget = QWidget()
            current = self.billboardDict[i]
            item = musicItem(current['song'], current['artist'], widget)
            # 리스트에 위젯 넣기
            billboardList.addItem(item)
            billboardList.setItemWidget(item, widget)
        for i in range(1,51):
            widget = QWidget()
            current = self.soundseaDict[i]
            item = musicItem(current['song'], current['artist'],  widget)
            # 리스트에 위젯 넣기
            koreanRankList.addItem(item)
            koreanRankList.setItemWidget(item, widget)
        
        billboardList.itemDoubleClicked.connect(Window.itemClicked) 
        koreanRankList.itemDoubleClicked.connect(Window.itemClicked) 
        self.setLayout(self.vbox5)

    def selectedListUpdate(self):
        title = self.sender().currentItem().getSongName()
        artist = self.sender().currentItem().getArtistName()
        L = [title,artist]
        widget = QWidget()
        item = musicItem(L[0],L[1],widget)
        self.currentMusicList.addItem(item)
        self.currentMusicList.setItemWidget(item, widget)
        h = hashlib.sha1()
        h.update((title +" "+artist).encode('utf-8'))
        file =  h.hexdigest() + ".mp3"
        directory = pData.getPath()
        playlist.append(directory + "\\" + file)

        pData.updateSelectedMusicDict({"song":title , "artist":artist , "filename": directory + "\\" + file })
        #print(playlist)

    def refreshButton1Clicked(self):
        pData.initDirectory()   
        directoryMusicDict = pData.getDirectoryMusicDict()

        self.myFileList.clear()
        for i in directoryMusicDict:
            widget = QWidget()
            current = directoryMusicDict[i]
            item = musicItem(current['song'], current['artist'], widget)
            # 리스트에 위젯 넣기
            self.myFileList.addItem(item)
            self.myFileList.setItemWidget(item, widget)


class musicItem(QListWidgetItem):
    def __init__(self, songName, artistName, widget):
        super().__init__()
        self.songName = QLabel("제목: " + songName)
        self.artistName = QLabel("가수: " + artistName)
        self.sender = [songName, artistName]
        vbox5 = QVBoxLayout()
        hbox8 = QHBoxLayout()
        hbox9 = QHBoxLayout()
        hbox8.addWidget(self.songName, alignment=Qt.AlignLeft)
        hbox9.addWidget(self.artistName, alignment=Qt.AlignLeft)
        vbox5.addLayout(hbox8)
        vbox5.addLayout(hbox9)
        widget.setLayout(vbox5)
        self.setSizeHint(widget.sizeHint())

    def getSongName(self):
        return self.songName.text().replace("제목: ","")
    
    def getArtistName(self):
        return self.artistName.text().replace("가수: ","")


def youtubeDownload(L):
    global pData
    print(L)
    pData.downloadMusic(L[1], L[0])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = Window()
    mywindow.show()
    app.exec_()