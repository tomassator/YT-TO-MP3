from django.shortcuts import render, HttpResponse
from ytmp3.funciones import conversor


# Create your views here.

convertidor = conversor.Convertidor()
def home(request):

    return render(request, "home.html")

#Vista de la subpagina como download
def download(request):
    if request.method == "GET":
        link = request.GET["linkYT"]
        convertidor.setLink(link)
        convertidor.setDatosVid()

    if request.method == "POST":
        formato = request.POST["btnquality"]
        itag = request.POST["inputCalidad{}".format(formato)]  #Itag es el id del video que usa el modulo pytube
        convertidor.descargar(itag, formato)

    return render(request, "download.html",{"info_mp3":convertidor.info_mp3, "info_mp4":convertidor.info_mp4, "info_vid":convertidor.info_vid})

#Vista de la subpagina como descargar
def comodescargar(request):
    return render(request, "comodescargar.html")


#{"info_mp3":info_mp3 , "info_mp4":info_mp4, "info_vid":info_vid})