from pytube import YouTube


# Funcion que devuelve el itag del audio junto con su informacion de calidad
def info_video_mp3(yt):
    mp3 = yt.streams.filter(file_extension="mp4", only_audio=True, mime_type="audio/mp4", adaptive=True)

    '''calidad_mp3 =[]
    for archivo in mp3:
        calidad_mp3.append((archivo.itag, archivo.abr))'''  #Se comenta el filtrado especifico del itag con la resolucion, se aplica lo mismo para las otras funciones.

    return mp3


# Funcion que devuelve el itag del video junto con su informacion de calidad
def info_video_mp4(yt):
    mp4 = yt.streams.filter(file_extension="mp4", mime_type="video/mp4", adaptive=True)

    '''calidad_mp4 = []
    for archivo in mp4:
        calidad_mp4.append((archivo.itag, archivo.resolution))'''

    return mp4


# Funcion que devuelve el itag del video con audio junto con su informacion de calidad
def info_video_vid(yt):
    vid = yt.streams.filter(file_extension="mp4", mime_type="video/mp4", progressive=True)

    '''calidad_vid = []
    for archivo in vid:
        calidad_vid.append((archivo.itag, archivo.resolution))'''

    return vid