import sys
import sip
import copy
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
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
        musicImage = QLabel(self)
        pixmap = QPixmap(self.imageDir+'black.png')
        pixmap = pixmap.scaled(800, 800, Qt.KeepAspectRatio)
        musicImage.setPixmap(pixmap)

        #슬라이더
        playSlider = QSlider()
        playSlider.setOrientation(Qt.Horizontal)
        playSlider.setMinimum(0)
        playSlider.setMaximum(1000)
        playSlider.setValue(0)
        playSlider.setStyleSheet(self.stylesheet())

        vbox1.addWidget(musicImage)
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

        self.pausePlayButton.toggled.connect(self.changeimage)

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

        #중간에 넣으려는 hboxsetting
        hboxsetting = QHBoxLayout()
        settingButton = QPushButton()
        settingButton.setFixedSize(30, 30)
        settingButton.setStyleSheet('background-color: #00ff0000')
        settingButton.setIcon(QIcon(self.imageDir+'gear.png'))
        #추후에 수정하기

        hboxsetting.addStretch(1)
        hboxsetting.addWidget(settingButton)
        hboxsetting.addStretch(1)
        vbox3.addLayout(hboxsetting)

        hbox3.addLayout(vbox3)

        #현재 재생목록 리스트 (hbox5)와 확장버튼 vbox4
        vbox4 = QVBoxLayout()
        hbox5 = QHBoxLayout()

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

        hbox5.addWidget(self.currentMusicList)

        l = [['나의 오랜 연인에게', '  다비치  '], ['헤어진 우리가 지켜야 할 것들', '  김나영, 양다일   '], ['Blueming', '  아이유 '],
             ['HIP', '  마마무(Mamamoo)  '], ['늦은 밤 너의 집 앞 골목길에서', '  노을  '], ['마음', '  폴킴  '],
             ['Into the Unknown (From "Frozen 2"/Soundtrack Ver.)', '  Idina Menzel, Aurora   '],
             ['FEVER (Feat. 수퍼비, BIBI)', '  박진영  '], ['Love poem', '  아이유  '],
             ['어떻게 이별까지 사랑하겠어, 널 사랑하는 거지', '  AKMU (악동뮤지션)  '], ['날 보러 와요 (Come See Me)', '  AOA  '],
             ['흔들리는 꽃들 속에서 네 샴푸향이 느껴진거야', '  장범준  '], ['안녕', '  폴킴  '],
             ['인기 (Feat. 송가인, 챈슬러)', '  MC몽  '], ['이 번호로 전화해줘', '  바이브  '],
             ['숨겨진\xa0세상\xa0(Into the Unknown End Credit Ver.) (“겨울왕국\xa02”)', '  태연 (TAEYEON)  '],
             ['시간의 바깥', '  아이유  '], ['Obsession', '  EXO  '],
             ['조금취했어 (Prod. 2soo)', '  임재현  '],
             ['Show Yourself (From "Frozen 2"/Soundtrack Ver.)', '  Idina Menzel, Evan Rachel Wood   '],
             ['새 사랑', '  송하예  '], ['오늘도 빛나는 너에게 (To You My Light) (Feat. 이라온)', '  마크툽(MAKTUB)  '],
             ['아마두 (Feat. 우원재, 김효은, 넉살, Huckleberry P)', '  염따, 딥 플로우, 팔로알토 (Paloalto), The Quiett, 사이먼 도미닉   '],
             ['운명이 내게 말해요', '  헤이즈 (Heize)  '], ['기억해줘요 내 모든 날과 그때를', '  거미  '], ['있어줘요', '장덕철  '],
             ['제목없음', '  황치열  '], ['불티 (Spark)', '  태연 (TAEYEON)  '], ['이별은 늘 그렇게 (Duet 정은지)', '허각  '],
             ['모든 날, 모든 순간 (Every day, Every Moment)', '  폴킴  '], ['영화 속에 나오는 주인공처럼', '  펀치 (Punch)  '],
             ['사랑이란 멜로는 없어', '  전상근  '], ['그 사람', '  아이유  '],
             ['내 생애 가장 행복한 시간 Part.2 (Feat. 양다일)', '  MC몽  '], ['샤넬 (Feat. 박봄)', '  MC몽  '], ['unlucky', '  아이유  ']]

        for i in l:
            widget = QWidget()
            item = musicItem(i[0],i[1],"시간시간시간",widget)
            #리스트에 위젯 넣기
            self.currentMusicList.addItem(item)
            self.currentMusicList.setItemWidget(item, widget)

        deleteItem = QListWidgetItem()
        deleteButtonWidget = QWidget()
        deleteHBox = QHBoxLayout()
        deleteButton = QPushButton("삭제")
        # deleteHBox.addStretch(1)
        deleteHBox.addWidget(deleteButton)
        deleteHBox.addStretch(1)
        deleteButtonWidget.setLayout(deleteHBox)
        deleteItem.setSizeHint(deleteButtonWidget.sizeHint())

        deleteButton.clicked.connect(self.listdelete)

        # self.currentMusicList.addItem(deleteItem)
        # self.currentMusicList.setItemWidget(deleteItem, deleteButtonWidget)


        vbox4.addLayout(hbox5)

        #스페이스랑 확장버튼
        hbox6 = QHBoxLayout()

        # 임시
        hbox6.addWidget(deleteButton)

        menuButton = QPushButton()
        menuButton.clicked.connect(self.expandWindow1)
        menuButton.setIcon(QIcon(self.imageDir+'plusbutton.png'))
        hbox6.addStretch(1)
        hbox6.addWidget(menuButton)

        vbox4.addLayout(hbox6)
        self.vbox5 = subWindow().sub1()

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
            self.vbox5 = subWindow().sub1()
            self.hbox1.addLayout(self.vbox5)

        self.isExpanded = not self.isExpanded    

    def sliderMoved(self):
        self.volumeValue.setText(str(self.volumeSlider.value()))

    def changeimage(self, pressed):

        self.pausePlayButton.setText({True: "❚❚", False: "▶"}[pressed])

    def deleteItemsOfLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)
                else:
                    self.deleteItemsOfLayout(item.layout())

    def boxdelete(self, layout, box):
        for i in range(layout.count()):
            layout_item = layout.itemAt(i)
            if layout_item.layout() == box:
                self.deleteItemsOfLayout(layout_item.layout())
                layout.removeItem(layout_item)
                break

    def listdelete(self):
        print(self.currentMusicList.currentItem().getSongName())
        for i in self.currentMusicList.selectedItems():
            self.currentMusicList.takeItem(self.currentMusicList.row(i))
        #print(listItems)

    #slider bar design
    def stylesheet(self):
        return """
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
        """

class subWindow:

    def __init__(self):
        self.initVariable()

    def initVariable(self):
        self.imageDir = "../../img/"

    def sub1(self):
        #확장 됬을때 self.vbox5
        self.vbox5 = QVBoxLayout()

        #검색 hbox7
        hbox7 = QHBoxLayout()
        searchInput = QLineEdit()
        searchInput.setStyleSheet('''
        background-color: #00ff0000;
        border: 2px solid black;
        border-width: 2px;
        border-color: black;
        ''')

        searchButton = QPushButton()
        searchButton.setStyleSheet('''
        background-color: #00ff0000;
        border-style: inset;
        border-width: 2px;
        border-radius: 10px;
        border-color: black;
        ''')

        searchButton.setFixedSize(30, 30)
        searchButton.setIcon(QIcon(self.imageDir+'magnifying-glass.png'))

        hbox7.addStretch(1)
        hbox7.addWidget(searchInput)
        hbox7.addWidget(searchButton)
        hbox7.addStretch(1)

        self.vbox5.addLayout(hbox7)

        #탭뷰
        tabs = QTabWidget()
        playListTab = QWidget()
        rankListTab = QWidget()
        myFileTab = QWidget()

        playListTab.setStyleSheet('''
        background-color: #00ff0000;
        border: 2px solid black;
        border-width: 3px;
        ''')
        rankListTab.setStyleSheet('''
        background-color: #00ff0000;
        border: 2px solid black;
        border-width: 3px;
        ''')
        myFileTab.setStyleSheet('''
        background-color: #00ff0000;
        border: 2px solid black;
        border-width: 3px;
        ''')

        tabs.addTab(playListTab, "재생 목록")
        tabs.addTab(rankListTab, "랭킹")
        tabs.addTab(myFileTab, "내 파일")

        self.vbox5.addWidget(tabs)

        return self.vbox5

class musicItem(QListWidgetItem):
    def __init__(self, songName, artistName, songTime, widget):
        super().__init__()
        self.songName = QLabel("제목: " + songName)
        self.artistName = QLabel("가수: " + artistName)
        self.songTime = QLabel("곡 시간: " + songTime)
        
        listVLayout = QVBoxLayout()
        listHLayout1 = QHBoxLayout()
        listHLayout2 = QHBoxLayout()
        listHLayout1.addWidget(self.songName, alignment=Qt.AlignLeft)
        # listHLayout1.addStretch(10)
        listHLayout2.addWidget(self.artistName, alignment=Qt.AlignLeft)
        listHLayout2.addWidget(self.songTime, alignment=Qt.AlignRight)
        listVLayout.addLayout(listHLayout1)
        listVLayout.addLayout(listHLayout2)
        widget.setLayout(listVLayout)
        self.setSizeHint(widget.sizeHint())

    def getSongName(self):
        return self.songName.text()
    
    def getArtistName(self):
        return self.songName.text()
    
    def getSongTime(self):
        return self.songTime.text()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = Window()
    mywindow.show()
    app.exec_()