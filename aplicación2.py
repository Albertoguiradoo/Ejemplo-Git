from tkinter import *
from tkinter import ttk
from pytube import YouTube

def  descargar():
    url=datos_entrada.get()
    youtube = YouTube(url) 
    youtube.author
    print(youtube.author)
    print("Descargando", youtube.title)
    cancion = youtube.streams.get_audio_only()
    cancion.download()

#Generar la ventana
ventana = Tk()
ventana.config(background="light blue")
ventana.title("Bienvenido a tu descargador favorito de canciones")
ventana.geometry("500x100")
ventana.resizable(width=False,height=False)



#Componentes Label y Button
títuloLabel = StringVar()
títuloLabel.set("url de la canción a descargar:")


espacio_para_url = ttk.Label(ventana, textvariable=títuloLabel)
espacio_para_url.config(background="aquamarine",border=5,font=("Arial",10))
espacio_para_url.place(x=10 ,y=20)

#Componente cuadro de texto 
datos_entrada=ttk.Entry(ventana)
datos_entrada.place(x=200, y=20)

ttk.Button(ventana, text="descargar", command=descargar).place(x=200, y=50)
ttk.Button(ventana, text="Salir", command=ventana.destroy).place(x=300, y=50)

ventana.mainloop()