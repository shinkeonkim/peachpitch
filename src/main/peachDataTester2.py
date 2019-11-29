from peachData import YoutubeDownloader

a = YoutubeDownloader("https://www.youtube.com//watch?v=VTd5kQhtih8","C:/Users/kimshinkeon/Desktop/peachpitch/src/example/pytube/")
a.start()
a.join()

for i in range(200):
    print("*")