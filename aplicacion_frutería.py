import flet as ft


def main(page: ft.Page):
    page.title="Bienvenido a su frutería de confianza!"
    def cambairTexto(z):
            t.value=textField_Nombre.value
            page.update()


        
        
    
    #Componente Texto
    t =ft.Text(value="Introducción a Flet", color="black", size=20)
    page.add(t)#add hace dos cosas: 1- Añadir 2- Actualizar
    

    t.value="Buenas caballero, ¿qué desea comprar?"
    
    
    #Componente Botón
    '''
    textField_Nombre= ft.TextField(label="Nombre",hint_text="Escribir tu nombre:")
    page.add(textField_Nombre)'''

    t.value="sección de verduras"
    page.update()
    
    bt= ft.FloatingActionButton(icon=ft.icons.ADD, on_click=cambairTexto)
    page.add(bt)

    dropDownMenú = ft.Dropdown(width=300, options=[ft.dropdown.Option("lechuga 0,9$/kg"),
                                                    ft.dropdown.Option("naranjas 2$/kg"),
                                                    ft.dropdown.Option("alcachofas 0,9$/kg"),
                                                    ft.dropdown.Option("mandarinas 2$/kg"),
                                                    ft.dropdown.Option("pepinillos 1,2$/kg"),
                                                    ft.dropdown.Option("tomate para el mejor gazpacho 2$/kg")])
    page.add(dropDownMenú)
    
   


ft.app(target=main)