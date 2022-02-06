from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=0f3ZHuC-l0c")

#print(yt.streams.filter(file_extension="mp4", only_audio=True)[0])
a = yt.streams.filter(file_extension="mp4", mime_type="video/mp4", adaptive=True)
arreglo=[]
for i in a:
    arreglo.append((i.itag,i.resolution))
print(a)