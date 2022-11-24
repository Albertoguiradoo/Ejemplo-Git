from tkinter import *
from tkinter import ttk

def saludar():
    texto = campoTexto.get()
    textoLabel.set(texto)


#Generar la ventana
ventana = Tk()
ventana.config(background="red")
ventana.title("Que pasa primo!")
ventana.geometry("500x500")
ventana.resizable(width=False,height=False)

imagen=PhotoImage(file="Espana.gif")
fondo=Label(ventana,image=imagen).place(x=10,y=15)

imagen2=PhotoImage(file="escudo.png")
fondo=Label(ventana,image=imagen2).place(x=55,y=15)

#Componentes Label y Button
textoLabel = StringVar()
textoLabel.set("Viva España!")
labelTexto = ttk.Label(ventana, textvariable=textoLabel)
labelTexto.config(background="yellow",border=5,font=("Arial",55))
labelTexto.pack()

#Componente cuadro de texto 
campoTexto=ttk.Entry(ventana)
campoTexto.pack()

ttk.Button(ventana, text="Saludos", command=saludar).pack()
ttk.Button(ventana, text="Salir", command=ventana.destroy).pack()

ventana.mainloop()