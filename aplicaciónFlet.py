import flet as ft


def main(page: ft.Page):
    page.title="Bienvenido!"
    def cambairTexto(z):
            t.value=textField_Nombre.value
            page.update()


        
        
    
    #Componente Texto
    t =ft.Text(value="Introducción a Flet", color="red", size=70)
    page.add(t)#add hace dos cosas: 1- Añadir 2- Actualizar
    

    t.value="Ferran balón de oro"
    page.update()
    #Componente Botón
    bt= ft.FloatingActionButton(icon=ft.icons.ADD, on_click=cambairTexto)

    textField_Nombre= ft.TextField(label="Nombre",hint_text="Escribir tu nombre:")
    textField_Nombre.focus()
    page.add(textField_Nombre)
    page.add(bt)











ft.app(target=main)