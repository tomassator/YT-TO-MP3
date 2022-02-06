from pytube import YouTube
from ytmp3.funciones import infovideos
import os

#Clase que se encargar de convertirel video a distintos formatos
class Convertidor():
    link = None
    yt = None
    info_mp3 = None
    info_mp4 = None
    info_vid = None


    #Setea el link ingresado por el usuario y llama a setYtObject
    def setLink(self, link):
        self.link=link
        self.setYtObject(link)

    #Seteamos el objeto video
    def setYtObject(self, link):
        self.yt = YouTube(link)

    #Metodo que setea la informacion de los formatos

    def setDatosVid(self):
        self.info_mp3 = self.get_calidad_mp3()
        self.info_mp4 = self.get_calidad_mp4()
        self.info_vid = self.get_calidad_vid()


    def get_calidad_mp3(self):
        return infovideos.info_video_mp3(self.yt)

    def get_calidad_mp4(self):
        return infovideos.info_video_mp4(self.yt)

    def get_calidad_vid(self):
        return infovideos.info_video_vid(self.yt)

    def descargar(self, itag, extension):
        self.yt.streams.get_by_itag(itag).download(filename=self.yt.title + "." + extension.lower())




