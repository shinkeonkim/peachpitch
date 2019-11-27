import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.imageDir = "../../img/"
        self.initUI()

    def initUI(self):
        self.setGeometry(100,100,1700,500)
        self.setWindowFlags(Qt.FramelessWindowHint)

        mainbox = QVBoxLayout()
        titlebox = QHBoxLayout()

        #타이틀바
        peachImage = QLabel(self)
        pixmap = QPixmap(self.imageDir+'peachpeachlogo.png')
        pixmap = pixmap.scaled(100, 100, Qt.KeepAspectRatio)
        peachImage.setPixmap(pixmap)
        minimizeButton = QPushButton("―")
        maximizeButton = QPushButton("□")
        closeButton = QPushButton("X")
        closeButton.clicked.connect(QCoreApplication.instance().quit)
        
        titlebox.addWidget(peachImage)
        titlebox.addSpacing(800)
        titlebox.addWidget(minimizeButton)
        titlebox.addWidget(maximizeButton)
        titlebox.addWidget(closeButton)

        mainbox.addLayout(titlebox)
        
        #재생과 리스트를 구분지을 수 있는 vbox넣기 위한 hbox1
        hbox1 = QHBoxLayout()
        
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

        self.pausePlayButton.setCheckable(True)

        self.pausePlayButton.toggled.connect(self.changeimage)

        hbox3.addWidget(prevSongButton)
        hbox3.addWidget(self.pausePlayButton)
        hbox3.addWidget(nextSongButton)

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
        hvolumeValue.addSpacing(69)
        hvolumeValue.addWidget(self.volumeValue)

        vbox2.addLayout(hvolumeValue)


        hbox4.addLayout(vbox2)
        hbox3.addLayout(hbox4)

        #설정버튼과 속도조절 vbox3
        vbox3 = QVBoxLayout()

        speedList = ["X 1.0", "X 0.25", "X 0.5", "X 0.75", "X 1.25", "X 1.5", "X 1.75", "X 2.0"]
        speedCombobox = QComboBox()
        for i in speedList:
            speedCombobox.addItem(i)

        vbox3.addWidget(speedCombobox)

        settingButton = QPushButton()
        settingButton.setIcon(QIcon(self.imageDir+'gear.png'))
        #추후에 수정하기

        vbox3.addWidget(settingButton)

        hbox3.addLayout(vbox3)

        #현재 재생목록 리스트 (hbox5)와 확장버튼 vbox4
        vbox4 = QVBoxLayout()
        hbox5 = QHBoxLayout()

        currentMusicList = QListWidget()
        currentMusicList.move(0,0)

        hbox5.addWidget(currentMusicList)

        vbox4.addLayout(hbox5)

        #스페이스랑 확장버튼
        hbox6 = QHBoxLayout()
        menuButton = QPushButton()
        menuButton.setIcon(QIcon(self.imageDir+'plusbutton.png'))

        hbox6.addSpacing(500)
        hbox6.addWidget(menuButton)

        vbox4.addLayout(hbox6)

        #확장 됬을때 vbox5
        vbox5 = QVBoxLayout()

        #검색 hbox7
        hbox7 = QHBoxLayout()
        searchInput = QLineEdit()
        searchButton = QPushButton()
        searchButton.setIcon(QIcon(self.imageDir+'magnifying-glass.png'))

        hbox7.addStretch(1)
        hbox7.addWidget(searchInput)
        hbox7.addWidget(searchButton)
        hbox7.addStretch(1)

        vbox5.addLayout(hbox7)

        #탭뷰
        tabs = QTabWidget()
        playListTab = QWidget()
        rankListTab = QWidget()
        myFileTab = QWidget()

        tabs.addTab(playListTab, "재생 목록")
        tabs.addTab(rankListTab, "랭킹")
        tabs.addTab(myFileTab, "내 파일")

        vbox5.addWidget(tabs)










        hbox1.addLayout(vbox1)
        hbox1.addLayout(vbox4)
        hbox1.addLayout(vbox5)
        mainbox.addLayout(hbox1)



        #메인 설정
        self.setLayout(mainbox)

    def sliderMoved(self):
        self.volumeValue.setText(str(self.volumeSlider.value()))

    def changeimage(self, pressed):

        self.pausePlayButton.setText({True: "❚❚", False: "▶"}[pressed])

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
                background: #fff;
                height: 40px;
            }

            QSlider::handle:horizontal {
                background: #bbf;
                border: 0px;
                width: 0px;
                margin-top: 0px;
                margin-bottom: 0px;
                border-radius: 0px;
            }
        """



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = Window()
    mywindow.show()
    app.exec_()