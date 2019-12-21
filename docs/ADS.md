# ADS(Architecture Design Specification)

## 모듈 설계
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

## 클래스 설계

### VIEW

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

### MODEL

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


### CONTROLLER

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

## Database 설계
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