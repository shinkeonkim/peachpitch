# DDS (Detailed Design Specification)

## VIEW

|클래스|메서드|입력 인자|입력 인자 타입|출력 인자|출력 인자 타입|기능|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| mainWindow | \_\_init\_\_ 생성자 |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |

## MODEL

### Class
|클래스|메서드|입력 인자|입력 인자 타입|출력 인자|출력 인자 타입|기능|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| billboardChart | \_\_init\_\_ 생성자 |   |   |  |  | self.billboardChartDict 선언music_database.db와 연결하는 self.conn 선언, self.conn의 cursor인 self.c 선언 |
| -- | initBillboardChart |  |  |  |  | 1. 빌보드차트 가져오고 <br> chart_billboard 테이블에 가수, 제목 저장 2. 테이블에 저장해논 가수, 제목들 self.billboardChartDict에 저장|
| -- | initBillboardChartDict |  |  |  |  | chart_billboard 테이블에 저장해논 가수, 제목들로 self.billboardChartDict 갱신|
| -- | getBillboardChartDict |  |  | self.billboardChartDict | dict() | 빌보드 차트 딕셔너리 반환 |
| soundseaChart | \_\_init\_\_ 생성자 |  |  |  |  | self.soundseaChartDict 선언 |
| -- | initSoundseaChartDict |  |  |  |  | 1. 소리 바다 차트 가져오고 <br> chart_soundsea 테이블에 가수, 제목 저장2. 테이블에 저장해논 가수, 제목들 self.soundseaChartDict에 저장  |
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

### Database
|TABLE| COLUMN | TYPE | NULL | Extra | descrption |
|:-:|:-:|:-:|:-:|:-:|:-:|
| chart_billboard | | | | | 빌보드 차트 top-100 노래 목록 table  |
| -- | id | INTEGER |  NOT NULL | PRIMARY_KEY | 차트 순위 |
| -- | song_name | TEXT | | | 노래 제목 |
| -- | artist_name | TEXT | | | 가수 이름 |
| -- | created_at | DATETIME | | | data 생성 시기 |
| chart_soundsea | | | | | 소리 바다 차트 top-50 노래 목록|
| -- | id | INTEGER |  NOT NULL | PRIMARY_KEY | 차트 순위 |
| -- | song_name | TEXT | | | 노래 제목 |
| -- | artist_name | TEXT | | | 가수 이름 |
| -- | created_at | DATETIME | | | data 생성 시기|
| directory_music  |  | | | |  | 사용자가 지정한 path에 있는 노래 목록 db |
| -- | id | INTEGER |  NOT NULL | PRIMARY_KEY | 노래 파일의 임의 ID |
| -- | song | TEXT |   |  | 노래 제목|
| -- | artist | TEXT |   |  | 가수 이름|
| -- | song_time | TEXT |   |  | 노래 재생 시간 |
| -- | file  | TEXT |   |  | 암호화된 mp3 파일의 이름 |
| setting |  |  |   |  | ||
| -- | billboard_chart_updated_at  | DATETIME |   |  | |빌보드 차트 db 최근 업데이트 시기 |
| -- | soundsea_chart_updated_at   | DATETIME |   |  | |  소리 바다 차트 db 최근 업데이트 시기|
| -- | path  | TEXT |   |  | 현재 프로그램이 돌아가고 있는 경로 |

# CONTROLLER

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