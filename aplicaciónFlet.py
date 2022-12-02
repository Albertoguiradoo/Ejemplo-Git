import flet as ft




def main(page: ft.Page):
    page.title="Bienvenido!"
    def cambairTexto(z):
        for i in range(10):
            te = ft.Text(value=f"texto número {i}", size= 20)
            page.add(te)


        
        
    
    #Componente Texto
    t =ft.Text(value="Introducción a Flet", color="red", size=70)
    page.add(t)#add hace dos cosas: 1- Añadir 2- Actualizar
    

    t.value="Ferran balón de oro"
    page.update()
    #Componente Botón
    bt= ft.FloatingActionButton(icon=ft.icons.ADD, on_click=cambairTexto)
    page.add(bt)











ft.app(target=main)