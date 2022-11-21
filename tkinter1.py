from tkinter import *
from tkinter import ttk

def saludar():
    texto = campoTexto.get()
    textoLabel.set(texto)


#Generar la ventana
ventana = Tk()
ventana.config(background="red")
ventana.title("Que pasa primo!")
ventana.geometry("1000x1000")
ventana.resizable(width=False,height=False)

imagen=PhotoImage(file="Espana.gif")
fondo=Label(ventana,image=imagen).place(x=100,y=150)

imagen2=PhotoImage(file="escudo.png")
fondo=Label(ventana,image=imagen2).place(x=550,y=150)


#Genera el liebnzo para pintar componentes
frm = ttk.Frame(ventana).pack()

#Componentes Label y Button
textoLabel = StringVar()
textoLabel.set("Viva España!")
labelTexto = ttk.Label(frm, textvariable=textoLabel)
labelTexto.config(background="yellow",border=5,font=("Arial",55))
labelTexto.pack()

#Componente cuadro de texto 
campoTexto=ttk.Entry(frm)
campoTexto.pack()

ttk.Button(frm, text="Saludos", command=saludar).pack()
ttk.Button(frm, text="Salir", command=ventana.destroy).pack()

ventana.mainloop()