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
| peachData | \_\_init\_\_ 생성자 |  |  |  |  | |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |



|클래스|메서드|입력 인자|입력 인자 타입|출력 인자|출력 인자 타입|기능|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| billboardChart | \_\_init\_\_ 생성자 | X | X | X | X |  |
| -- | initBillboardChart | X | X | X | X | 1. 빌보드차트 가져오고 <br> chart_billboard 테이블에 가수, 제목 저장 2. 테이블에 저장해논 가수, 제목들 self.billboardChartDict에 저장 self. |
| -- | initLink |  |  |  |  | 1. Crawling할 쓰레드들 미리 만듬. 만들 때 target을 PeachTube 클래스의 YoutubeCrawling 메서드로함. 2. 크롤링을 한 반복문에서 진행하고 db의 char_billboard, self.billboardChartDict에 반영 |
| -- | getBillboardChartDict | x | x | self.billboardChartDict | dict() | 빌보드 차트 딕셔너리 반환 |

|클래스|메서드|입력 인자|입력 인자 타입|출력 인자|출력 인자 타입|기능|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| soundseaChart | \_\_init\_\_ 생성자 | X | X | X | X |  |
| -- | initSoundseaChart | X | X | X | X | 1. 소리 바다 차트 가져오고 <br> chart_soundsea 테이블에 가수, 제목 저장 2. 테이블에 저장해논 가수, 제목들 self.soundseaChartDict에 저장 self. |
| -- | initLink |  |  |  |  | 1. Crawling할 쓰레드들 미리 만듬. 만들 때 target을 PeachTube 클래스의 YoutubeCrawling 메서드로함. 2. 크롤링을 한 반복문에서 진행하고 db의 char_soundsea, self.soundseaChartDict에 반영 |
| -- | getSoundseaChartDict | x | x | self.soundseaChartDict | dict() | 소리바다 차트 딕셔너리 반환 |

|클래스|메서드|입력 인자|입력 인자 타입|출력 인자|출력 인자 타입|기능|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| peachTube | \_\_init\_\_ 생성자 |  |  |  |  |  |
| -- | YoutubeCrawling |  |  |  |  |  |
|  | YoutubeDownload | link | str |  |  | 다운로드를 하고 파일을 mp3로 변환한다음, 파일의 이름을 hash 시키고 문자열 return |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |


|클래스|메서드|입력 인자|입력 인자 타입|출력 인자|출력 인자 타입|기능|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|  | \_\_init\_\_ 생성자 |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |

# CONTROLER