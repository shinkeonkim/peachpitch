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
|--|  |  |
|--|  |  |
|--|  |  |
|methods|  |  |
|--|  |  |
|--|  |  |
|--|  |  |

### musicPlayer

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
