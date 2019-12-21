# DDS (Detailed Design Specification)

## Main.py

### Window

|--| 이름 | 역할, 설명 | 
|:--:|:--:|:--:|
|attributes| | |
|--|  |  |
|--|  |  |
|--|  |  |
|methods|  |  |
|--|  |  |
|--|  |  |
|--|  |  |

### subWindow

|--| 이름 | 역할, 설명 | 
|:--:|:--:|:--:|
|attributes| | |
|--|  |  |
|--|  |  |
|--|  |  |
|methods|  |  |
|--|  |  |
|--|  |  |
|--|  |  |

### settingWindow

|--| 이름 | 역할, 설명 | 
|:--:|:--:|:--:|
|attributes| | |
|--|  |  |
|--|  |  |
|--|  |  |
|methods|  |  |
|--|  |  |
|--|  |  |
|--|  |  |

### musicItem

|--| 이름 | 역할, 설명 | 
|:--:|:--:|:--:|
|attributes| | |
|--|  |  |
|--|  |  |
|--|  |  |
|methods|  |  |
|--|  |  |
|--|  |  |
|--|  |  |

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
|--| updateSelectedMusicDict |  |
|--| initDirectory |  |
|--| getDirectoryMusicDict |  |
|--| downloadMusic |  |

### musicPlayer

|--| 이름 | 역할, 설명 | 
|:--:|:--:|:--:|
|attributes| | |
|--| player | QMediaPlayer() 객체이고 노래을 재생시킬 때 사용한다. |
|--| playlist | QMediaPlayList() 객체이고 노래 재생 목록 관련 객체이다.  |
|methods|  |  |
|--| \_\_init\_\_ | |
|--| getPlayer |  |
|--| play |  |
|--| pause |  |
|--| stop |  |
|--| prev |  |
|--| next |  |
|--| createPlaylist |  |
|--| updatePlayMode |  |
|--| updateVolume |  |
|--| mediaChanged |  |

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
|--|  |  |
|--|  |  |
|--|  |  |
|methods|  |  |
|--|  |  |
|--|  |  |
|--|  |  |

### searchTube

|--| 이름 | 역할, 설명 | 
|:--:|:--:|:--:|
|attributes| | |
|--|  |  |
|--|  |  |
|--|  |  |
|methods|  |  |
|--|  |  |
|--|  |  |
|--|  |  |
