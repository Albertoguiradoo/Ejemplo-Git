from tkinter import *
from tkinter import ttk
from tkinter import messagebox

usuario= ""
contraseña= ""
contraseña2= ""
vNum= []
def guardarDAtos():
    usuario = entry_nombre_usuario.get()
    contraseña= entry_contraseña.get()
    contraseña2=entry_contraseña_repetir.get()
    if contraseña == contraseña2:
        print(f"Usuario: {usuario}\ncontraseña: {contraseña2}")
        vNum.append(usuario)
        vNum.append(contraseña)
        messagebox.showinfo("Usuario guardado",f"Usuario {usuario} guardado :)")
    else:
        print("Las contraseñas no coinciden, por favor intentelo de nuevo")
    
#Generar la ventana

ventana = Tk()
ventana.config(background= "light blue")
ventana.geometry("400x200")
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

botón_guardar.grid(row=4, column=0, pady= 5)
botón_salir.grid(row=4, column=1, pady= 5)
ventana.mainloop()