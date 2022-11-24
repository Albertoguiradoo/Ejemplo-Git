from tkinter import *
from tkinter import ttk

#Generar la ventana

ventana = Tk()
ventana.config(background= "light blue")
ventana.geometry("500x500")
ventana.resizable(width=FALSE, height=FALSE)

#Titulo de la aplicación

ventana.title("Ventana de registro")

#Título de la ventana

label_título = ttk.Label(ventana, text="Datos del Usuario")

#Componentes para pedir los datos

label_nombre_usuario= ttk.Label(ventana, text="Nombre Usuario: ")
entry_nombre_usuario= ttk.Entry(ventana)

label_contraseña= ttk.Label(ventana, text="Contraseña: ")
entry_contraseña= ttk.Entry(ventana)

label_contraseña_repetir= ttk.Label(ventana, text="Repite la contraseña: ")
entry_contraseña_repetir= ttk.Entry(ventana)

botón_guardar= ttk.Label(ventana, text="Guardar")
botón_salir= ttk.Label(ventana, text= "Salir")

#Pintar en pantalla los componentes
label_título.grid(row=0, column=1, pady= 2)

label_nombre_usuario.grid(row=1, column=0, pady= 2)
entry_nombre_usuario.grid(row=1, column=1, pady= 2)

label_contraseña.grid(row=2, column=0, pady= 2)
entry_contraseña.grid(row=2, column=1, pady= 2)

label_contraseña_repetir.grid(row=3, column=0, pady= 2)
entry_contraseña_repetir.grid(row=3, column=1, pady= 2)

botón_guardar.grid(row=4, column=0, pady= 2)
botón_salir.grid(row=4, column=1, pady= 2)

ventana.mainloop()