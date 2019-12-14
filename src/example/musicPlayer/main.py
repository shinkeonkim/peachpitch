from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import QAudioProbe, QMediaPlayer
import sys
from player import *
 
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
 
class CWidget(QWidget):   
 
    def __init__(self):
        super().__init__()
        self.player = CPlayer(self)
        self.playlist = []
        self.selectedList = [0]
        self.playOption = QMediaPlaylist.Sequential

        self.setWindowTitle('Ocean Coding School')
        self.audiop = QAudioProbe()

        self.initUI()
    
    def picture(self):
        L = self.sender()
        print(L)


    def initUI(self):
 
        vbox = QVBoxLayout()        
 
        # 1.Play List
        box = QVBoxLayout()
        gb = QGroupBox('Play List')
        vbox.addWidget(gb)
         
        self.table = QTableWidget(0, 2, self)             
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem('Title'))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem('Progress')) 
        # read only
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # single row selection
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        # signal 
        self.table.itemSelectionChanged.connect(self.tableChanged)
        self.table.itemDoubleClicked.connect(self.tableDbClicked)
        box.addWidget(self.table)
         
        hbox = QHBoxLayout()
        btnAdd = QPushButton('Add List')
        btnDel = QPushButton('Del List')
        btnAdd.clicked.connect(self.addList)
        btnDel.clicked.connect(self.delList)
        hbox.addWidget(btnAdd)
        hbox.addWidget(btnDel)   
         
        box.addLayout(hbox)
        gb.setLayout(box)        
         
        # 2.Play Control
        box = QHBoxLayout()
        gb = QGroupBox('Play Control')
        vbox.addWidget(gb)
 
        text = ['◀◀', '▶', '⏸', '▶▶', '■']
        grp = QButtonGroup(self)
        for i in range(len(text)):
            btn = QPushButton(text[i], self)            
            grp.addButton(btn, i)
            box.addWidget(btn)
        grp.buttonClicked[int].connect(self.btnClicked)
 
        # Volume
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setRange(0,100)
        self.slider.setValue(50)
        self.slider.valueChanged[int].connect(self.volumeChanged)
        box.addWidget(self.slider)        
        gb.setLayout(box)
 
        # 3.Play Option
        box = QHBoxLayout()
        gb = QGroupBox('Play Option')
        vbox.addWidget(gb)       
 
        str = ['current item once', 'current item in loop', 'sequential', 'loop', 'random']
        grp = QButtonGroup(self)
        for i in range(len(str)):
            btn = QRadioButton(str[i], self)
            if i==QMediaPlaylist.Sequential:
                btn.setChecked(True)
            grp.addButton(btn, i)  
            box.addWidget(btn)        
         
        grp.buttonClicked[int].connect(self.radClicked)
             
        gb.setLayout(box)               
         
        self.setLayout(vbox)
        self.show()
 
    def tableChanged(self):
        self.selectedList.clear()        
        for item in self.table.selectedIndexes():
            self.selectedList.append(item.row())
         
        self.selectedList = list(set(self.selectedList))
         
        if self.table.rowCount()!=0 and len(self.selectedList) == 0:
            self.selectedList.append(0)
        #print(self.selectedList)
 
    def addList(self):
        files = QFileDialog.getOpenFileNames(self
                                             , 'Select one or more files to open'
                                             , ''
                                             , 'Sound (*.mp3 *.wav *.ogg *.flac *.wma)')        
        cnt = len(files[0])       
        row = self.table.rowCount()        
        self.table.setRowCount(row + cnt)
        for i in range(row, row+cnt):
            self.table.setItem(i,0, QTableWidgetItem(files[0][i-row]))
            pbar = QProgressBar(self.table)
            pbar.setAlignment(Qt.AlignCenter)            
            self.table.setCellWidget(i,1, pbar)
             
        self.createPlaylist()       
 
    def delList(self):        
        row = self.table.rowCount()      
 
        index = []       
        for item in self.table.selectedIndexes():
            index.append(item.row())        
         
        index = list(set(index))        
        index.reverse()        
        for i in index:
            self.table.removeRow(i)
         
        self.createPlaylist()       
 
    def btnClicked(self, id):
         
        if id==0: #◀◀
            self.player.prev()
        elif id==1: #▶
            if self.table.rowCount()>0:
                self.player.play(self.playlist, self.selectedList[0], self.playOption)
        elif id==2: #⏸
            self.player.pause()
        elif id==3: #▶▶
            self.player.next()
        else: #■
            self.player.stop()
 
    def tableDbClicked(self, e):
        self.player.play(self.playlist, self.selectedList[0], self.playOption)
 
    def volumeChanged(self):
        self.player.upateVolume(self.slider.value())
 
    def radClicked(self, id):
        self.playOption = id
        self.player.updatePlayMode(id)
 
    def paintEvent(self, e):
        self.table.setColumnWidth(0, self.table.width()*0.7)
        self.table.setColumnWidth(1, self.table.width()*0.2)
 
    def createPlaylist(self):
        self.playlist.clear()
        for i in range(self.table.rowCount()):
            self.playlist.append(self.table.item(i,0).text())
 
        #print(self.playlist)
 
    def updateMediaChanged(self, index):
        if index>=0:
            self.table.selectRow(index)            
 
    def updateDurationChanged(self, index, msec):        
        #print('index:',index, 'duration:', msec)
        self.pbar = self.table.cellWidget(index, 1)
        if self.pbar:
            self.pbar.setRange(0, msec)       
 
    def updatePositionChanged(self, index, msec):
        self.audiop.setSource(self.player.getPlayer())
        self.audiop.audioBufferProbed(QAudioBuffer = 10).connect(self.picture)
        #print('index:',index, 'position:', msec)
        self.pbar = self.table.cellWidget(index, 1)
        if self.pbar:
            self.pbar.setValue(msec)
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CWidget()
    sys.exit(app.exec_())