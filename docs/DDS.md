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

|클래스|메서드|입력 인자|입력 인자 타입|출력 인자|출력 인자 타입|기능|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| billboardChart | \_\_init\_\_ 생성자 | X | X | X | X | self.billboardChartDict 선언 |
| -- | initBillboardChartDict | X | X | X | X | 1. 빌보드차트 가져오고 <br> chart_billboard 테이블에 가수, 제목 저장 2. 테이블에 저장해논 가수, 제목들 self.billboardChartDict에 저장|
| -- | getBillboardChartDict | x | x | self.billboardChartDict | dict() | 빌보드 차트 딕셔너리 반환 |

|클래스|메서드|입력 인자|입력 인자 타입|출력 인자|출력 인자 타입|기능|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| soundseaChart | \_\_init\_\_ 생성자 | X | X | X | X | self.soundseaChartDict 선언 |
| -- | initSoundseaChartDict | X | X | X | X | 1. 소리 바다 차트 가져오고 <br> chart_soundsea 테이블에 가수, 제목 저장2. 테이블에 저장해논 가수, 제목들 self.soundseaChartDict에 저장  |
| -- | getSoundseaChartDict | x | x | self.soundseaChartDict | dict() | 소리바다 차트 딕셔너리 반환 |

|클래스|메서드|입력 인자|입력 인자 타입|출력 인자|출력 인자 타입|기능|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| peachTube | \_\_init\_\_ 생성자 | directory_path | str |  |  | self.directory_path에 directory_path 저장|
| -- | SearchSong |          |     |            |         | "https://www.youtube.com/results?search_query=" 에 songName과 artist를 더해 조회하고 유효한 첫번째 동영상의 링크를 return 한다.  |
| -- | -- | songName | str |            |         |    |
| -- | -- |  artist  | str |            |         |    | 
| -- |        --       |          |     |  videoLink |   str   |    |
|  | musicDownload |  |  |  |  | 다운로드를 하고 파일을 mp3로 변환한다음, 파일의 이름을 암호화시키고 암호화처리한 파일의 이름을 directoryMusicDict 에 추가한다.({{"song": 제목, "artist": 가수, "filename" : 디렉토리 + 파일 이름}, ... }) |
|  | -- | link | str |  |  | 다운로드할 유튜브 영상의 링크 |
|  | -- | directoryMusicDict | dict()의 레퍼런스 |  |  | 다운로드하고 난뒤 정보를 저장할 딕셔너리 |
|  | -- | path  | str | | | mp3 파일을 저장할 파일 경로(path) | 


# CONTROLER

|클래스|메서드|입력 인자|입력 인자 타입|출력 인자|출력 인자 타입|기능|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| peachData | \_\_init\_\_ 생성자 |  |  |  |  | |
| --  | --  |  |  |  |  | self. |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |