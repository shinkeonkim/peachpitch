# 최종 보고서

## 조원
### 소개
| name | student_id | github_username |
|:----:|:--------:|:-----------------:|
|김신건|20191564|shinkeonkim|
|김은수|20191568|Eun-Su-Kim|

### 역할 분담
| name | role |
|:--:|:--:|
|김신건| DB 제작, 크롤링, 노래 다운 기능 |
|김은수| UI 구성, 제작, 백엔드와 연결 |

## 주제
```
pyqt를 이용한 뮤직 플레이어, peachpitch
```
### peachpitch란
```
복숭아를 나타내느 peach와 음높이를 나타내는 pitch를 합친 말이며, 
복숭아 음악 플레이어를 의미합니다.
```
## 제작 동기
```
음악이란 것은 실생활에서 정말 많은 곳에서 경험하는 매체입니다. 이런 매체를 재생하는 것은 음악 플레이어입니다. 한번 실생활에서 많이 접하고 사용하는 음악플레이어를 2학기 동안 배운 PYQT를 활용해 제작해보자는 생각을 하게 되었고 바로 실행으로 옮기게 되었습니다.
```


## 계획

### SRS(Software Requirement Specification)

#### 1. 기능적 요구사항

- [ ] 1.1 음악 재생 기능
    - [ ] 1.1.1. 웹에서 받아온 음악
        - [ ] 1.1.1.1. 음악 스트리밍
        - [x] 1.1.1.2. 다운로드된 음악

    - [x] 1.1.2. 사용자 디렉토리에 있는 음악 재생

    - [x] 1.1.3. 노래 속도 제어
        - [x] 1.1.3.1. (0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2) 배속을 제어한다.
    
    - [x] 1.1.4. 사용자가 선택한 음악 목록에서 음악 선택 기능
        - [x] 1.1.4.1. 더블클릭으로 음악을 선택한다.

    - [x] 1.1.5. 재생 버튼을 누르면 노래가 재생, 재생 버튼은 일시정지 버튼으로 바뀜

    - [x] 1.1.6. 뒷트랙 버튼을 누르면 현재 곡을 처음으로 되돌아가고, 현재 곡이 0초에서 1초 사이에 버튼을 누르면 재생목록의 이전곡을 재생

- [ ] 1.2. 음악 재생목록 기능
    
- [ ] 1.3. 음악 별점 기능

- [ ] 1.4. 설정 기능
    - [ ] 1.4.1. (인터페이스를 밝게 어둡게)
    - [ ] 1.4.2. 모든 노래를 노동요로 듣기(모든 노래 1.5배속 기본 설정)
    - [ ] 1.4.3. (음악에 가사 넣기)

- [ ] 1.5. 정렬 기능
    - [ ] 1.5.1. 내가 매긴 별점순
    - [ ] 1.5.2. 웹에서의 순위순
        - [ ] 1.5.2.1. 웹의 종류에 따라 순위가 달라지며 받아오는 시점은 1. 프로그램을 처음 실행할때, 2. 새로고침 버튼을 누를때이다.
    - [ ] 1.5.3. 재생수
        - [ ] 1.5.3.1. 재생수의 기준은 내가 선택한 기준으로 한다. 노래가 끝나고 자동으로 다음 노래로 넘어갔을 때에는 재생수가 오르지 않는다.

- [x] 1.6. 검색 기능
    - [x] 1.6.1. 디렉토리 내 검색 결과와 웹에서의 검색결과를 보여준다.

- [x] 1.7. 사용자 데이터 저장 기능
    - [x] 1.7.1. 사용자가 갖고 있는 음악 목록
    - [ ] 1.7.2. 음악 별점 저장
    - [ ] 1.7.3. 재생수 저장
    - [ ] 1.7.4. 재생목록
    - [x] 1.7.5. 사용자 설정 저장
    - [ ] 1.7.6. 가사 저장

#### 2. 사용자 인터페이스 요구사항

- [ ] 2.1. 음악 재생과 관련된 인터페이스를 구성하는 요소는 다음과 같다.  
    - [x] 2.1.1. 재생 버튼 / 일시정지 버튼
    - [ ] 2.1.2. 정지 버튼  
    - [x] 2.1.3. 앞트랙 버튼  
    - [x] 2.1.4. 뒷트랙 버튼  
    - [x] 2.1.5. 재생 바  
    - [x] 2.1.6. 볼륨 조절 
        - [x] 2.1.6.1. 볼륨 조절 다이얼
    - [x] 2.1.7. 재생 속도 조절
        - [x] 2.1.7.1. 재생 속도 콤보 박스
        - [x] 2.1.7.1. 재생 속도 목록(1.0, 0.25, 0.5, 0.75, 1.25, 1.5, 1.75, 2.0)
    - [x] 2.1.8. 썸네일 또는 영상
        - [x] 2.1.8.1. 영상 무한 재생
    - [x] 2.1.9. 설정 버튼
        - [ ] 2.1.9.1. 모든 노래를 노동요로 듣기 체크박스
        - [ ] 2.1.9.2. 인터페이스 밝기 조절 바
        - [ ] 2.1.9.3. (음악에 가사넣기)
    - [ ] 2.1.10. 가사 보기 버튼
    - [ ] 2.1.11. 별점(숫자) 체크

- [x] 2.2. 음악 목록과 관련된 인터페이스를 구성하는 요소는 다음과 같다.  
    - [x] 2.2.1. 최근에 담은 음악 목록
    - [x] 2.2.2. 차트 목록
        - [x] 2.2.2.1. 다운로드한 음악 목록
            - [x] 2.2.2.1.1. 음악 목록 갱신 버튼
        - [x] 2.2.2.2. 빌보드 차트 목록
        - [x] 2.2.2.3. 소리 바다 차트 목록
    - [x] 2.2.3. 검색창

#### 3. 비기능적 요구사항
    
- [x] 3.1. 이 소프트웨어의 구현에는 Python과 PyQt5를 이용한다.
- [x] 3.2. 사용자의 컴퓨터에는 ffmpeg.exe의 환경변수가 등록되어 있어야 한다.
- [x] 3.3. 사용자의 컴퓨터에 chrome이 설치되어 있어야 하며 설치된 chrome에 맞는 chromedriver.exe가 필요하다.


### ADS(Architecture Design Specification)

#### 모듈 설계
| 모듈 | 클래스 | 역할|
|:--:|:--:|:--:|
| Main | Window | 백이랑 연결된 UI |
| -- | subWindow | UI중 확장됬을때의 부분 |
| -- | musicItem | 리스트에 넣을 item들 |
| -- | settingWindow | 설정창 |
| peach_controller  | peachData  | 모든 음악 정보, 설정 관련 기능을 총괄함. |
| -- | musicPlayer | 음악 재생 기능을 총괄함. 
| peach_model | billboardChart | 빌보드 차트 정보와 관련된 model |
|  | soundseaChart | 소리 바다 차트 정보와 관련된 model |
|  | selectedMusicDict  | 사용자가 선택(다운)한 노래 관련 model |
|  | peachTube | pytube를 이용해 아티스트, 노래 제목을 이용해 노래를 검색하고 mp4로 파일을 받고 mp3로 변환함. |
| | searchTube | 사용자가 직접 지정한 문자열로 노래를 검색한 검색 결과를 다룸 |

#### 클래스 설계

##### VIEW

|클래스|메서드|입력 인자|입력 인자 타입|출력 인자|출력 인자 타입|기능|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Window | \_\_init\_\_ 생성자 |  |  |  |  | pData, playlist, billboardChartDict, soundseaChartDict, directoryMusicDict, selectedMusicDict 선언|
| -- |initVariable  |  |  |  |  |  |
| -- | initUI |  |  |  |  | 사용자에게 UI의 모습을 보여줌 |
| -- | boxdelete | layout, box | layout |  |  | layout내의 box를 지운다. |
| -- | listdelete |  |  |  |  | 사용자의 플레이리스트에서 더블클릭된 아이템을 삭제한다. |
| -- | deleteItemsOfLayout | layout | layout |  |  | 한 레이아웃에서 존재하는 아이템을 삭제하고 만약 아이템이 레이아웃이라면 재귀적으로 호출하여 삭제한다. |
| -- | itemClicked |  |  |  |  | 차트에서 음악 정보가 더블클릭되었을 때, 노래를 다운로드한다. |
| -- | currentMusicListItemDoubleClicked |  |  |  |  | 현재음악리스트아이템을 더블클릭했을때 재생되게 한다. |
| -- | sliderMoved |  |  |  |  | 현재 노래의 볼륨을 컨트롤 |
| -- | changeImage |  |  |  |  | 재생 버튼을 누르면 재생 일시정지 이미지 바뀌고 현재 재생되는 노래의 정보를 갱신하고 화면의 재생 여부를 결정한다. |
| -- | updateMediaChanged | index | int |  |  | 현재 선택된 노래로 재생한다. |
| -- | prev |  |  |  |  | 이전 곡 재생 |
| -- | next |  |  |  |  | 다음 곡 재생 |
| -- | mediaPlayerStatusChanged |  |  |  |  | 동영상 종료됬을때 다시 재생하게 함 |
| -- | getCurrentPlaying |  |  |  |  | 현재 재생하고 있는 노래의 정보를 return 한다. |
| -- | setCurrentPlaying | title, artist | str |  |  | 현재재생라벨에 제목하고 가수를 적는다. |
| -- | settingWindowPopup |  |  |  |  | 설정창을 띄운다. |
| -- | getEncodefilename | title, artist | str | sha1str | str | path, title, artist를 이용해 파일의 이름을 암호화시킨 문자열을 return 한다. |
| subWindow | \_\_init\_\_ 생성자 | billboardDict, soundseaDict, currentMusicList | dict |  |  | initVariable 호출, self.billboardDict, self.soundseaDict, self.currentMusicList에 각각 매개변수로 초기화 |
| -- | initVariable |  |  |  |  | self.imageDir 초기화(이미지 저장된 디렉토리), self.conn, self.c 초기화|
| -- | initUI |  |  |  |  | 확장버튼을 눌렀을때 확장된 창의 모습을 보여줌 |
| -- | webSearchDownload |  |  |  |  | 웹 검색 결과에서 사용자가 선택한 영상을 다운로드하고 노래로 변환한다. 그리고 db에 노래 정보를 반영한다. |
| -- | searchClicked |  |  |  |  | 웹 검색 결과에서 더블 클릭했을 때의 이벤트를 받아들이는 메서드이다 |
| -- | selectedListUpdate |  |  |  |  | 다운로드된 음악 리스트에서 특정 아이템을 더블클릭하면 재생 목록으로 update(add)해준다. |
| -- | getEncodefilename | title, artist | sha1str | str |  | path,title,artist를 이용해 암호화된 노래 파일 이름을 return 한다. |
| -- | refreshButton1Clicked |  |  |  |  | 새로고침 버튼이 눌렸을때, db의 정보를 초기화하고 새로 directoryMusicDict의 정보를 반영한다. |
| musicItem | \_\_init\_\_ | songName, artistName, widget |  |  |  | 리스트 아이템 추가 |
| -- | getSongName |  |  |  |  | 곡 제목을 가져옴 |
| -- | getArtistName |  |  |  |  | 가수 이름을 가져옴 |
| settingWindow | \_\_init\_\_ |  |  |  |  | 윈도우 타이틀 아이콘 설정 |
| -- | initUI |  |  |  |  | 설정창을 보여줌 |

##### MODEL

|클래스|메서드|입력 인자|입력 인자 타입|출력 인자|출력 인자 타입|기능|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| billboardChart | \_\_init\_\_ 생성자 |   |   |  |  | self.billboardChartDict 선언music_database.db와 연결하는 self.conn 선언, self.conn의 cursor인 self.c 선언 |
| -- | initBillboardChart |  |  |  |  | 1. 빌보드차트 가져오고 <br> chart_billboard 테이블에 가수, 제목 저장 2. 테이블에 저장해논 가수, 제목들 self.billboardChartDict에 저장|
| -- | initBillboardChartDict |  |  |  |  | chart_billboard 테이블에 저장해논 가수, 제목들로 self.billboardChartDict 갱신|
| -- | getBillboardChartDict |  |  | self.billboardChartDict | dict() | 빌보드 차트 딕셔너리 반환 |
| soundseaChart | \_\_init\_\_ 생성자 |  |  |  |  | self.soundseaChartDict 선언 |
| -- | initSoundseaChart |  |  |  |  | 1. 소리 바다 차트 가져오고 <br> chart_soundsea 테이블에 가수, 제목 저장2. 테이블에 저장해논 가수, 제목들 self.soundseaChartDict에 저장  |
| -- | initSoundseaChartDict  |  | ||| 테이블에 저장해논 가수, 제목들 self.soundseaChartDict에 갱신|
| -- | getSoundseaChartDict |  |  | self.soundseaChartDict | dict() | 소리바다 차트 딕셔너리 반환 |
| peachTube | \_\_init\_\_ 생성자 | directory_path | str |  |  | self.directory_path에 directory_path 저장|
| -- | searchSong |          |     |            |         | "https://www.youtube.com/results?search_query=" 에 songName과 artist를 더해 조회하고 유효한 첫번째 동영상의 링크를 return 한다.  |
| -- | -- | songName | str |            |         |    |
| -- | -- |  artist  | str |            |         |    | 
| -- |        --       |          |     |  videoLink |   str   |    |
|  | musicDownload |  |  |  |  | 다운로드를 하고 파일을 mp3로 변환한다음, 파일의 이름을 암호화시키고 암호화처리한 파일의 이름을 directoryMusicDict 에 추가한다.({{"song": 제목, "artist": 가수, "filename" : 디렉토리 + 파일 이름}, ... }) |
|  | -- | link | str |  |  | 다운로드할 유튜브 영상의 링크 |
|  | -- | directoryMusicDict | dict()의 레퍼런스 |  |  | 다운로드하고 난뒤 정보를 저장할 딕셔너리 |
|  | -- | path  | str | | | mp3 파일을 저장할 파일 경로(path) | 
| selectedMusic | | | | | | |
| -- | \_\_init\_\_ 생성자 | | | | | self.selectedMusicDict 선언 |
| -- | initSelectedMusicDict | | | | | selectedMusicDict 딕셔너리 selected_music 테이블에서 정보 받아와서 초기화 |
| -- | addMusic | music_dict | dict() | |  | 노래 추가(딕셔너리, DB 모두 추가됨) |
| -- | deleteMusic | music_dict | dict() | | | 노래 삭제(딕셔너리, DB 모두 삭제됨) |
| -- | getSelectedMusicDict | self.selectedMusicDict | dict() | | | 전체 노래 딕셔너리 반환 |


##### CONTROLLER

|클래스|메서드|입력 인자|입력 인자 타입|출력 인자|출력 인자 타입|기능|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| peachData | \_\_init\_\_ 생성자 |  |  |  |  | 1. self.directoryMusicDict(dict()),  self.path(str) 선언 2. billboardChart 객체, soundseaChart 객체, peachTube 객체 선언|
| --  | setPath | path | str |  |  | self.path에 path 저장 |
| -- | initChart |  |  |  |  | billboardChart 객체의 initBillboardChart 메서드 호출, soundseaChart 객체의 initSoundseaChart 메서드 호출 |
| -- | initChartDict |  |  |  |  | billboardChart 객체의 initBillboardChartDict 메서드 호출, soundseaChart 객체의 initBillboardChartDict 메서드 호출  |
| -- | initDirectory  |  |  |  |  | self.path가 빈 문자열이 아니라면 self.path에 있는 파일들을 탐색하고 directory_music DB 테이블을 참조해서 directoryMusicDict을 초기화함. |
| -- | getDirectoryMusicDict |  |  |  |  | self.directoryMusicDict 반환함 |
| -- | downloadMusic |  |  |  |  | song, artist를 받아서 peachTube 객체의 searchSong 메서드, musicDownload 메서드 호출, 다운로드 완료한 다음에 initDirectory 호출|
| -- | -- | song | str |  |  | 다운로드할 노래 제목 |
| -- | -- | artist | str |  |  | 다운로드할 노래의 가수 |

#### Database 설계
|TABLE| COLUMN | TYPE | NULL | Extra | descrption |
|:-:|:-:|:-:|:-:|:-:|:-:|
| chart_billboard | | | | | 빌보드 차트 top-100 노래 목록 table  |
| -- | id | INTEGER |  NOT NULL | PRIMARY KEY | 차트 순위 |
| -- | song_name | TEXT | | | 노래 제목 |
| -- | artist_name | TEXT | | | 가수 이름 |
| -- | created_at | DATETIME | | | data 생성 시기 |
| chart_soundsea | | | | | 소리 바다 차트 top-50 노래 목록|
| -- | id | INTEGER |  NOT NULL | PRIMARY KEY | 차트 순위 |
| -- | song_name | TEXT | | | 노래 제목 |
| -- | artist_name | TEXT | | | 가수 이름 |
| -- | created_at | DATETIME | | | data 생성 시기|
| directory_music  |  | | | |  | 사용자가 지정한 path에 있는 노래 목록 db |
| -- | id | INTEGER |  NOT NULL | PRIMARY KEY AUTOINCREMENT | 노래 파일의 임의 ID |
| -- | song_name | TEXT |   |  | 노래 제목|
| -- | artist_name | TEXT |   |  | 가수 이름|
| -- | file_name  | TEXT |   |  | 암호화된 mp3 파일의 이름 |
| -- | created_at | DATETIME |   |  | | DB상 노래가 생성된 시기 |
| selected_music | | | | | | |
| -- | id | INTEGER |  NOT NULL | PRIMARY KEY AUTOINCREMENT | 노래 파일의 임의 ID |
| -- | song_name | TEXT |   |  | 노래 제목|
| -- | artist_name | TEXT |   |  | 가수 이름|
| -- | file_name  | TEXT |   |  | 암호화된 mp3 파일의 이름 |
| -- | created_at | DATETIME |   |  | | DB상 노래가 생성된 시기 | 
| setting |  |  |   |  | ||
| -- | billboard_chart_updated_at  | DATETIME |   |  | |빌보드 차트 db 최근 업데이트 시기 |
| -- | soundsea_chart_updated_at   | DATETIME |   |  | |  소리 바다 차트 db 최근 업데이트 시기|
| -- | path  | TEXT |   |  | 현재 프로그램이 돌아가고 있는 경로 |


### DDS (Detailed Design Specification)

#### Main.py

##### Window

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


##### subWindow

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
|methods| webSearchDownload | 웹에서 검색한 것을 다운로드 한다. |
|--| searchClicked | 검색한 검색 결과를 list에 반영한다. |
|--| selectedListUpdate | 선택한 것을 현재 재생목록에 추가한다. |
|--| getEncodefilename | directory, artsit, title을 이용해 암호화된 sha1문자열을 만들어 return한다. |
|--| refreshButton1Clicked | 새로고침을 누르면 내 파일의 목록을 바꾼다. |

##### settingWindow

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

##### musicItem

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

#### peach_controller.py

##### peachData

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

##### musicPlayer

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

#### peach_model.py

##### billboardChart

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

##### soundseaChart

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

##### selectedMusicDict

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

##### peachTube

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

##### searchTube

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


## 구현 내용

### 1. UI구성된 BOX들

<img src = "../img/mainbox.png">
<img src = "../img/addbox.png">
<img src = "../img/setbox.png">

### 2. 메인 화면

<img src = "../img/Window.png">

### 3. 확장된 메인 화면

<img src = "../img/addWindow.png">

### 4. 빌보드 차트, 한국차트 기

<img src = "../img/billboardchart.png">
<img src = "../img/koreanchart.png">

### 5. 검색 기능
<img src = "../img/searching.png">

### 6. 재생 목록

<img src = "../img/musiclist.png">

### 7. 설정창
<img src = "../img/settingwindow.PNG">

## 느낀점
### 김신건
```
하나의 GUI 프로그램을 만드는 상황 속에 모든 구현을 python만을 이용하자는 생각으로 시작하게 되었다.
이에  DB(sqlite3), 크롤링 코드(selenium,beautifulsoup4,chrome driver), 특수한 모듈(pytube, thread, billboard, subprocess) 등을 사용하게 되었고 python에 대한 많은 공부를 할 수 있었습니다. 또한, PYQT를 이용해 프로그램을 제작하면서 GUI에 대한 기초 또한 알 수 있었습니다.

```
### 김은수
```
python만으로도 여러가지가 가능하다 라는걸 느낄 수 있었다.
하나의 프로그램을 만드는데 고려해야 할 것이 생각보다 더 많구나 라는 것을 느낄 수 있었고, 팀원간의 협동플레이가 확실히 중요하다라는 것을 느끼게 해준 AD프로젝트 였던 것 같다. 내 입장에서는 이런식으로 덩치가 큰 프로그램을 만드는 것이 처음이었는데, 내가 아직 많이 부족하고, 더 공부해야겠다는 생각이 들게 된 과제였다.
```
