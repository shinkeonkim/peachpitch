# DDS (Detailed Design Specification)

## Main.py

### Window

|--| 이름 | 역할, 설명 | 
|:--:|:--:|:--:|
|attributes| pData | peach_controller의 peachData 클래스의 객체 |
|--| playlist | 재생해야 할 노래의 목록 |
|--| billboardChartDict | billboardChart 노래를 담아두는 딕셔너리 |
|--| soundseaChartDict | 소리바다 차트 노래를 담아두는 딕셔너리 |
|--| directoryMusicDict | 디렉토리에 다운로드받은 노래 목록을 담아두는 딕셔너리 |
|--| selectedMusicDict | 재생목록에 선택된 노래 목록 |
|--| conn | music_database.db 파일과 connect해주는 속성 |
|--| c | connd의 cursor 속성 |
|--| self.player | peach_controller의 musicPlayer 객체 |
|--| self.playOption | 노래를 재생하는 옵션을 결졍하는 속성 |
|--| self.mediaPlayer | 비디오를 재생시키는 QMediaPlayer 객체 |
|--| self.imageDir | 이미지 경로를 설정한다. |
|--| mainbox | UI의 메인부분을 담당한다. |
|--| titlebox | 타이틀 부분을 담당한다. |
|--| peachImage | 피치의 로고 위치를 담당한다. |
|--| pixmap | 피치로고를 지정한다. |
|--| minimizeButton | 최소화 버튼이다. |
|--| closeButton | 닫기 버튼이다. |
|--| self.hbox1 | 재생부분과 리스트 부분을 구분짓는다. |
|--| vbox1 | 노래를 재생하면 나오는 영상이랑 재생버튼이 있는 레이아웃이다. |
|--| videoWidget | 노래를 재생하면 나오는 영상 객체이다. |
|--| self.playslider | 재생바의 객체이다. |
|--| hbox2 | 재생버튼이랑 볼륨 설정을 나눌 레이아웃이다. |
|--| hbox3 | 재생버튼들을 나눌 레이아웃이다. |
|--| prevSongButton | 이전 노래 버튼이다. |
|--| nextSongButton | 다음 노래 버튼이다. |
|--| self.pausePlayButton | 재생 버튼이다. |
|--| hbox4 | 볼륨설정이랑 설정 버튼이 있는 레이아웃이다. |
|--| vbox2 | 볼륨설정이 있는 레이아웃이다. |
|--| hbolumeValue | 볼륨의 value를 알려주는 레이아웃이다. |
|--| self.volumeSlider | 볼륨 다이얼이다. |
|--| self.volumeValue | 볼륨의 value를 알려주는 레이아웃이다. |
|--| vbox3 | 설정버튼이랑 속도조절이 있는 레이아웃이다. |
|--| speedList | 속도 조절 목록의 리스트이다. |
|--| self.speedCombobox | 속도 조절할 콤보박스이다. |
|--| hbox5 | 설정버튼을 가운데에 놓기 위한 레이아웃이다. |
|--| self.settingButton | 설정버튼이다. |
|--| vbox4 | 현재 재생목록 리스트랑 확장버튼이 있는 레이아웃이다. |
|--| hbox6 | 현재 재생목록 리스트를 넣은 레이아웃이다. |
|--| self.currentPlayingLabel | 현재 재생하고 있는 노래의 정보를 알려주는 라벨이다. |
|--| self.currentMusicList | 현재 재생목록 리스트이다. |
|--| hbox7 | 확장버튼이랑 삭제 버튼이 있는 레이아웃이다. |
|--| deleteButton | 현재 재생목록의 노래를 삭제하는 버튼이다. |
|--| menuButton | 내 파일과 랭킹 탭을 볼 수있는 창을 확장 시키는 버튼이다. |
|--| self.vbox5 | 확장 되었을 때의 레이아웃이다. |
|methods| | |
|--|speedComboboxCurrnetIndexChangedEvent | 노래의 속도를 조절한다. |
|--| positionChanged |  노래가 재생될 때, playerSlider의 바또한 진행한다. |
|--| durationChanged | playerSlide의 범위를 노래의 길이로 조정한다. |
|--| setPosition | playerSlider가 움직이면 player의 position을 조정한다. |
|--| handleError | 에러가 난 경우 에러메시지를 출력한다. |
|--| mousePressEvent | 창을 누르는 위치를 조절한다. |
|--| mouseMoveEvent | 창을 누르는 위치 조절과 창을 움직일 수 있게 한다. |
|--| expandWindow1 | 창을 확장시킨다. |
|--| boxdelete | 확장된 창을 삭제한다. |
|--| listdelete | 선택된 노래를 재생목록에서 삭제한다. |
|--| deleteItemsOfLayout | layout에 들어있는 item들 모두 삭제한다. 만약 item이 아닌 layout인 경우 재귀적으로 호출해 안에 있는 item을 계속 지워나간다.|
|--| itemClicked | 버튼이 클릭됬을때, 노래를 다운로드한다. |
|--| currentMusicListItemDoubleClicked | 재생목록 노래에서 특정 노래가 더블클릭되었을때, 기존 노래를 정지하고 노래를 클릭된 노래로 재생한다.|
|--| sliderMoved | 재생바의 움직임을 담당한다. |
|--| changeImage | 재생 아이콘과 일시정지 아이콘을 바꾼다. |
|--| updateMediaChanged | 노래 목록을 갱신시킨다. |
|--| prev | 이전 노래로 바꾸게 한다. |
|--| next | 다음 노래로 바꾸게 한다. |
|--| mediaPlayerStatusChanged | 재생하면 나오는 영상이 멈췄을때 다시 틀게 한다. |
|--| getCurrentPlaying | 현재 재생하고 있는 노래의 라벨을 가져온다. |
|--| setCurrentPlaying | 현재 재생하고 있는 노래의 라벨을 바꾼다. |
|--| settingWindowPopup | 설정창이 뜨게 한다. |
|--| getEncodefilename | directory, artsit, title을 이용해 암호화된 sha1문자열을 만들어 return한다. |


### subWindow

|--| 이름 | 역할, 설명 | 
|:--:|:--:|:--:|
|attributes| self.vbox5 | 확장된 창의 메인 레이아웃이다. |
|--| self.tabs | 탭을 만든다. |
|--| self.myFileTab | 탭의 요소를 담당한다. |
|--| self.rankListTab | 탭의 요소를 담당한다. |
|--| self.searchingTab | 탭의 요소를 담당한다. |
|--| self.tvbox1 | 파일탭뷰 안에서의 레이아웃이다. |
|--| self.thbox1 | 검색할 수 있는 위젯을 넣는 레이아웃이다. |
|--| self.refreshButton1 | 새로고침 버튼이다. |
|--| self.myFileSearchInput | 검색할 수 있는 검색창이다. |
|--| self.myFileSearchButton | 검색 할 수 있는 검색창의 버튼이다. |
|--| self.myFileList | 내 파일의 리스트이다. |
|--| self.tvbox2 | 랭킹 탭뷰 안에서의 레이아웃이다. |
|--| self.thbox2 | 빈공간을 주기 위한 레이아웃이다. |
|--| self.rankTab | 랭킹들이 나오는 탭이다. |
|--| billboardList | 랭킹 탭 안의 빌보드 리스트이다. |
|--| koreanRankList | 랭킹 탭 안의 한국 리스트이다. |
|--| self.nullSpace | 빈공간이다. |
|--| self.tvbox3 | 검색 탭뷰 안에서의 레이아웃이다. |
|--| self.thbox3 | 제목을 넣을 수 있는 레이아웃이다. |
|--| self.thbox4 | 가수를 넣을 수 있는 레이아웃이다. |
|--| self.webSearchingTitleInput | 제목을 넣는 검색창이다. |
|--| self.webSearchingArtistInput | 가수를 넣는 검색창이다. |
|--| self.webSearchingButton | 검색하는 버튼이다. |
|--| self.webSearchView | 검색 결과가 나오는 리스트이다. |
|methods| webSearchDownload | **웹에서 검색한 것을 다운로드 한다. |
|--| searchClicked | **검색한 것을 누르면 나오냐??????? |
|--| selectedListUpdate | **선택한 것을 현재 재생목록에 추가한다. |
|--| getEncodefilename | ** |
|--| refreshButton1Clicked | **새로고침을 누르면 내 파일의 목록을 바꾼다. |

### settingWindow

|--| 이름 | 역할, 설명 | 
|:--:|:--:|:--:|
|attributes| | |
|--| self.imageDir | img 폴더 경로 지정  |
|--| self.settingBox | 설정창의 레이아웃이다. |
|--| self.shbox1 | 설정창 목록의 레이아웃이다. |
|--| self.sakeLLabel | 설정창의 내용이다. |
|methods|  |  |
|--| \_\_init\_\_ | attribute 초기화, initUI 호출 |
|--| initUI | UI 초기화 |

### musicItem

|--| 이름 | 역할, 설명 | 
|:--:|:--:|:--:|
|attributes| | |
|--| self.songName | "제목: 노래 이름"의 text를 가진 QLabel|
|--| self.artistName | "가수: 가수 이름"의 text를 가진 QLabel |
|--| sender | sender 속성을 상속바다 쉐도잉한다. [songName, artistName]의 문자열을 담은 리스트 객체가 저장된다. |
|--| vbox5 | 리스트 아이템에서의 레이아웃이다. |
|--| hbox8 | 리스트 아이템에서의 제목 레이아웃이다. |
|--| hbox9 | 리스트 아이템에서의 가수 레이아웃이다. |
|methods|  |  |
|--|\_\_init\_\_| attrubute 초기화, UI  초기화|
|--| getSongName | "제목: " 문자열을 제외한 노래 제목 문자열 return |
|--| getArtistName | "가수: "문자열을 제외한 노래 제목 문자열 return |

## peach_controller.py

### peachData

|--| 이름 | 역할, 설명 |
|:--:|:--:|:--:|
|attributes| | |
|--| path | Main.py 혹은 peach_controller.py가 실행되는 디렉토리 정보 |
|--| billBoardChart | peach_model의 billboardChart 객체이다.  |
|--| soundseaChart | peach_model의 soundseaChart 객체이다. |
|--| selectedMusic | peach_model의 selectedMusicDict 객체이다. |
|--| directoryMusicDict | 디렉토리에 저장된 음악을 나열한 딕셔너리이다. |
|--| conn | music_database.db 파일과 connect해주는 속성 |
|--| c | connd의 cursor 속성 |
|methods|  |  |
|--| \_\_init\_\_ | attributes들을 초기화한다. |
|--| setPath | path를 임의로 주어진 문자열로 지정한다. |
|--| getPath | path를 return한다. |
|--| initChart | 모든 차트 정보의 db, 딕셔너리를 초기화한다. 그리고 선택한 음악 딕셔너리도 초기화한다.  |
|--| initChartDict | 모든 차트 정보의 딕셔너리를 초기화한다. 그리고 선택한 음악 딕셔너리도 초기화한다. |
|--| getBillboardChartDict | billBoardChart 객체의 getBillboardChartDict 메서드 결과를 return 한다. |
|--| getSoundseaChartDict | soundseaChart 객체의 getSoundseaChartDict 메서드 결과를 return 한다. |
|--| getSelectedMusicDict | selectedMusicDict 객체의 getSelectedMusicDict 메서드 결과를 return 한다. |
|--| getSelectedMusicPlaylist | selectedMusic 객체의 getSelectedMusicDict 메서드의 결과를 이용해 암호화된 파일 이름을 나열한 list  |
|--| updateSelectedMusicDict | 매개변수로 들어오는 dict에 노래를 추가한다. |
|--| initDirectory | 디렉토리에 있는 음악 파일의 정보를 db에서 정보를 얻어와 slef.directoryMusicDict를 갱신한다. |
|--| getDirectoryMusicDict |self.directoryMusicDict를 return 한다. |
|--| downloadMusic | artist와 song을 파라미터로 받아 peachtube 객체를 선언하고 start() 메서드를 실행한다.  |

### musicPlayer

|--| 이름 | 역할, 설명 | 
|:--:|:--:|:--:|
|attributes| | |
|--| player | QMediaPlayer() 객체이고 노래을 재생시킬 때 사용한다. |
|--| playlist | QMediaPlayList() 객체이고 노래 재생 목록 관련 객체이다.  |
|methods|  |  |
|--| \_\_init\_\_ | attribute 초기화 |
|--| getPlayer | self.player 를 return함. |
|--| play | playlist와 시작점을 파라미터로 받아서 playlist에서 시작점부터 재생하도록 한다. |
|--| pause | 노래 일시정지 |
|--| stop | 노래 정지 |
|--| prev | 이전 노래로 이동 |
|--| next | 다음 노래로 이동 |
|--| createPlaylist | playlist 새로 갱신하기 위한 메서드 |
|--| updatePlayMode | 베속을 조절하는 메서드 |
|--| updateVolume | 볼륨을 갱신한다. |
|--| mediaChanged |  부모의 updateMediaChanged로 플레이리스트의 현재 재생중인 index를 전달한다. |

## peach_model.py

### billboardChart

|--| 이름 | 역할, 설명 | 
|:--:|:--:|:--:|
|attributes| | |
|--| billboardCharDict | 빌보드 차트 음악 정보가 담기는 딕셔너리, {number:{"song": title, "artist":artist}} 와 같은 형태이다.|
|--| conn | music_database.db 파일과 connect해주는 속성 |
|--| c | connd의 cursor 속성 |
|methods|  |  |
|--| \_\_init\_\_ | billboardChart의 attribute 초기화 |
|--| initBillboardChart | billboard 모듈의 ChartData('hot-100')를 이용해 hot 100위를 초기화한다. 초기화한 정보를 music_database.db에 갱신하고 self.billboardChartDict에도 반영한다. |
|--| initBillboardChartDict | music_database.db에 있는 정보를 self.billboardChartDict에 반영한다.(db를 최근 갱신했다는 것이 확인되면 굳이 database를 갱신시키지 않아도 되기때문에) |
|--| getBillboardChartDict | self.billboardChartDict 리턴함|
|--| setUpatedAt | 빌보드 차트 정보를 database에 갱신시킨 datetime을 database의 SETTING 테이블에 갱신함.  |

### soundseaChart

|--| 이름 | 역할, 설명 | 
|:--:|:--:|:--:|
|attributes| | |
|--| soundseaChartDict|소리바다 차트 음악 정보가 담기는 딕셔너리, {number:{"song": title, "artist":artist}} 와 같은 형태이다.|
|--| conn | music_database.db 파일과 connect해주는 속성 |
|--| c | connd의 cursor 속성 |
|methods|  |  |
|--| \_\_init\_\_ | soundseaChart의 attribute 초기화 |
|--| initSoundseaChart | 셀레니움, 크롬드라이버를 이용해 소리바다 사이트를 크롤링하고 소리바다 top 50 노래 정보를 초기화한다. 초기화한 정보를 music_database.db에 갱신하고 self.soundseaChartDict에도 반영한다. |
|--| initSoundseaChartDict | music_database.db에 있는 정보를 self.soundseaCharttDict에 반영한다.(db를 최근 갱신했다는 것이 확인되면 굳이 database를 갱신시키지 않아도 되기때문에) |
|--| getSoundseaChartDict | self.soundseaChartDict 리턴함|
|--| setUpatedAt | 소리바다 차트 정보를 database에 갱신시킨 datetime을 database의 SETTING 테이블에 갱신함.  |

### selectedMusicDict

|--| 이름 | 역할, 설명 | 
|:--:|:--:|:--:|
|attributes| | |
|--| selectedMusicDict|, {number:{"song": title, "artist":artist , "file_name":sha1string}} 와 같은 형태이다.|
|--| conn | music_database.db 파일과 connect해주는 속성 |
|--| c | connd의 cursor 속성 |
|methods|  |  |
|--| initSelectedMusicDict | selectedMusicDict의 attribute 초기화 |
|--| addMusic | 사용자 선택 노래 목록에 노래 추가 |
|--| deleteMusic | 사용자 선택 노래 목록에서 노래 삭제 |
|--| getSelectedMusicDict | 사용자 선택 목록(selectedMusicDict) return |

### peachTube

|--| 이름 | 역할, 설명 | 
|:--:|:--:|:--:|
|attributes| | |
|--| directory_path | 다운로드할 디렉토리 |
|--| artist | 가수 문자열 |
|--| title | 노래 제목 문자열 |
|--| filename | 암호화된 파일 이름 문자열 |
|methods|  |  |
|--| \_\_init\_\_ |  |
|--| searchSong | 노래와 가수를 검색한 youtube 검색 결과에서 유효한 첫번째 영상의 링크를 반환한다.|
|--| run | threadong.Tread 객체의 메서드 오버라이딩, pytube의 다운로드 메서드 이용해서 다운받고 ffmpeg로 동영상 파일을 mp3로 변환|

### searchTube

|--| 이름 | 역할, 설명 | 
|:--:|:--:|:--:|
|attributes| | |
|--| directory_path | 다운로드할 디렉토리 |
|--| artist | 가수 문자열 |
|--| title | 노래 제목 문자열 |
|--| filename | 암호화된 파일 이름 문자열 |
|--| searchlink | 검색 링크|
|methods|  |  |
|--| \_\_init\_\_ |  |
|--| run | threadong.Tread 객체의 메서드 오버라이딩, 주어진 링크의 영상을  pytube의 다운로드 메서드 이용해서 다운받고 ffmpeg로 동영상 파일을 mp3로 변환|
