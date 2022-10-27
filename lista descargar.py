from pytube import Playlist
def descargarLista(url:str):
    playlist = Playlist(url)
    for cancion in playlist:
        print(cancion)

url= "https://www.youtube.com/playlist?list=PLn4HIQeUB9iL8Nj_2DgLCF42VVNfUJfOG"
descargarLista(url)

