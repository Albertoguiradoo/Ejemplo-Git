'''
edad = 5

edad_como_texto = str(edad)
edad= int(edad_como_texto)

print(edad/5)

print(len("Juan"))

edad2 = int(input("Dime tu edad:"))

#---Funciones definidas por el usuario

def imprimirHola(nombre:str, apellido:str):
    print("Hola ",nombre,apellido)

imprimirHola("Juan", "Zamora")


def imprimirSuma(num1:int, num2:int):
    #print("La suma de", num1, "+", num2,"=", num1+num2)
    return num1+num2

suma=imprimirSuma(2,3)
print("La suma es de: ", suma)
'''

from pytube import Playlist
from pytube import YouTube
def  descargarCAncion(url:str):
    youtube = YouTube(url) 
    youtube.author
    print(youtube.author)
    print("Descargando", youtube.title)
    cancion = youtube.streams.get_audio_only()
    cancion.download()

descargarCAncion("https://youtu.be/5MTiv9UGAhQ")

from pytube import Playlist
def descargarLista(url:str):
    playlist = Playlist(url)
    
    for cancion in playlist.videos:
        print("Descargando cacion: ", cancion.title)
        cancion.streams.get_audio_only().download("canciones/")
        print("****************\n")

url= "https://www.youtube.com/playlist?list=PLn4HIQeUB9iL8Nj_2DgLCF42VVNfUJfOG"
descargarLista(url)


