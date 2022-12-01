from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

usuario= ""
contraseña= ""
contraseña2= ""
genero=""
vNum= []
def guardarDAtos():
    genero=combo_género .get()
    usuario = entry_nombre_usuario.get()
    contraseña= entry_contraseña.get()
    contraseña2=entry_contraseña_repetir.get()
    if contraseña == contraseña2:
        print(f"Usuario: {usuario}\ncontraseña: {contraseña2}\ngénero:{genero}")
        vNum.append(usuario)
        vNum.append(contraseña)
        vNum.append(genero)
        messagebox.showinfo("Usuario guardado",f"Usuario {usuario} guardado :)")
    
    else:
        print("Las contraseñas no coinciden, por favor intentelo de nuevo")
    
#Generar la ventana

ventana = Tk()
ventana.config(background= "light blue")
ventana.geometry("500x300")
ventana.resizable(width=FALSE, height=FALSE)

#Titulo de la aplicación

ventana.title("Ventana de registro")

#Título de la ventana

label_título = ttk.Label(ventana, text="Datos del Usuario")

#Componentes para pedir los datos

label_nombre_usuario= ttk.Label(ventana, text="Nombre Usuario: ")
entry_nombre_usuario= ttk.Entry(ventana)

label_contraseña= ttk.Label(ventana, text="Contraseña: ")
entry_contraseña= ttk.Entry(ventana, show=" ")
 
label_contraseña_repetir= ttk.Label(ventana, text="Confirma la contraseña: ")
entry_contraseña_repetir= ttk.Entry(ventana,show=" ")

label_género= ttk.Label(ventana, text="Género:")

botón_guardar= ttk.Button(ventana, text="Guardar", command=guardarDAtos)
botón_salir= ttk.Button(ventana, text= "Salir", command=ventana.destroy)

#Pintar en pantalla los componentes
label_título.grid(row=0, column=1, pady= 5)

label_nombre_usuario.grid(row=1, column=0, pady= 5)
entry_nombre_usuario.grid(row=1, column=1, pady= 5)

label_contraseña.grid(row=2, column=0, pady= 5)
entry_contraseña.grid(row=2, column=1, pady= 5)

label_contraseña_repetir.grid(row=3, column=0, pady= 5,padx=15)
entry_contraseña_repetir.grid(row=3, column=1, pady= 5)

botón_guardar.grid(row=5, column=0, pady= 6)
botón_salir.grid(row=5, column=1, pady= 6)

label_género.grid(row=4, column=0, pady= 5)

#Combobox   
combo_género = ttk.Combobox(ventana, values=["Mujer", "Hombre", "Género no binario", "No espeficicar"])
combo_género .grid(row=4, column=1, pady= 5)
combo_género.set("Espeficique su género")



ventana.mainloop()