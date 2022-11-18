from tkinter import *
from tkinter import ttk
#Generar la ventana
ventana = Tk()
ventana.config(background="aquamarine")
ventana.title("Que pasa primo!")
ventana.geometry("500x500")
ventana.resizable(width=False,height=False)
imagen=PhotoImage(file="Espana.gif")
fondo=Label(ventana,image=imagen).place(x=0,y=0)

#Genera el liebnzo para pintar componentes
frm = ttk.Frame(ventana).pack()

#Componentes Label y Button
labelTexto = ttk.Label(frm, text="Viva España!")
labelTexto.config(background="light blue",border=5,font=("Arial",15))
labelTexto.pack()
ttk.Button(frm, text="Salir", command=ventana.destroy).pack()


ventana.mainloop()