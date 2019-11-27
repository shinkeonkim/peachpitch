from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=9bZkp7q19f0')
#yt.streams.filter(only_audio=True).first().download()
yt.streams.filter(only_audio=True).order_by('abr').asc().first().download('C:\\Users\\kimshinkeon\\Desktop\\peachpitch\\video')