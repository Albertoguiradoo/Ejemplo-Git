import flet as ft


def main(page: ft.Page):
    page.title="Bienvenido!"
    def cambairTexto(z):
            t.value=textField_Nombre.value
            page.update()


        
        
    
    #Componente Texto
    t =ft.Text(value="Introducción a Flet", color="red", size=70)
    page.add(t)#add hace dos cosas: 1- Añadir 2- Actualizar
    

    t.value="Brasil gana el mundial"
    page.update()
    #Componente Botón
    bt= ft.FloatingActionButton(icon=ft.icons.ADD, on_click=cambairTexto)

    textField_Nombre= ft.TextField(label="Nombre",hint_text="Escribir tu nombre:")
    page.add(textField_Nombre)
    page.add(bt)
    dropDownMenú = ft.Dropdown(width=100, options=[ft.dropdown.Option("argentina")])
    page.add(dropDownMenú)
    dropDownMenú.options.append(ft.dropdown.Option("Nueva"))
    page.update()

    slider_edad= ft.Slider(min=0,max=130 ,divisions=130,label="Edad: {value}", )
    page.add(slider_edad)    


ft.app(target=main)