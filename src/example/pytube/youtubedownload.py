import os
import subprocess

import pytube

yt = pytube.YouTube("https://www.youtube.com/watch?v=eI8wbCNq-G8") 

"""
vids= yt.streams.all()

for i in range(len(vids)):
    print(i,'. ',vids[i])

vnum = int(input())
vids[vnum].download(parent_dir)

"""
parent_dir = "C:/Users/kimshinkeon/Desktop/peachpitch/src/example/pytube/video/"
parent_dir2 = "C:/Users/kimshinkeon/Desktop/peachpitch/src/example/pytube/audio/"

vids = yt.streams.filter(mime_type = "video/mp4").first()

default_filename = vids.default_filename
print(default_filename)

vids.download(parent_dir)

new_filename = "test.wav"

subprocess.Popen(['ffmpeg', '-i', parent_dir + default_filename, parent_dir2 + new_filename])

print('다운로드 되었습니다!')
"""
from pytube import YouTube
import os
from moviepy.editor import *

yt = YouTube('https://www.youtube.com/watch?v=eI8wbCNq-G8') #다운로드 받고자 하는 url을 입력합니다.
 
print(yt.title)
yt.streams.first().download()
directory = "C:\\Users\\kimshinkeon\\Desktop\\peachpitch\\src\\example"
"""