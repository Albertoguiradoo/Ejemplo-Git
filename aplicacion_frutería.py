import flet as ft


def main(page: ft.Page):
    page.title="Bienvenido a su frutería de confianza!"
    
    def finalizar_Compra():
        print(vCompra)


    
 
    
    
    vCompra=[]
    def añadir_producto(e):
        if dropDownMenúVerduras.value!=None:
            vCompra.append(dropDownMenúVerduras.value)
            dropDownMenúVerduras.clean
        else:
            print("No ha seleccionado nada.")
        
    botón_Añadir_Verduras=ft.FilledButton(text="Añadir", icon="Añadir", on_click=añadir_producto)
    botón_Añadir_Carnes=ft.FilledButton(text="Añadir", icon="Añadir", on_click=añadir_producto)
    botón_Añadir_Pescados=ft.FilledButton(text="Añadir", icon="Añadir", on_click=añadir_producto)
    botón_Añadir_Sales=ft.FilledButton(text="Añadir", icon="Añadir", on_click=añadir_producto)
    botón_Añadir_Cervezas=ft.FilledButton(text="Añadir", icon="Añadir", on_click=añadir_producto)
    botón_Añadir_Botellas=ft.FilledButton(text="Añadir", icon="Añadir", on_click=añadir_producto)
    botón_Finalizar_Compra=ft.FilledButton(text="Finalizar Compra", icon="Añadir", on_click=finalizar_Compra)
      


    #Componente Texto
    texto_Título =ft.Text(value="Buenas caballero, ¿qué desea comprar?", color="black", size=20)
    page.add(texto_Título)#add hace dos cosas: 1- Añadir 2- Actualizar
    
    texto_Título_Sección_Verduras=ft.Text(value="sección de Verduras", color="black", size=20)
    page.add(texto_Título_Sección_Verduras)


    dropDownMenúVerduras = ft.Dropdown(width=300, options=[ft.dropdown.Option("lechuga 0,9$/kg"),
                                                    ft.dropdown.Option("naranjas 2$/kg"),
                                                    ft.dropdown.Option("alcachofas 0,9$/kg"),
                                                    ft.dropdown.Option("moras 50$/kg"),
                                                    ft.dropdown.Option("pepinillos 1,2$/kg"),
                                                    ft.dropdown.Option("tomate para el mejor gazpacho 2$/kg")])
    fila1 = ft.Row(spacing=50, controls=[dropDownMenúVerduras,botón_Añadir_Verduras] )                                             
    page.add(fila1)
    slider_Kilos_Verduras=ft.Slider(min=0, max=5000,divisions=5000, label="Gramos{value}")
    page.add(slider_Kilos_Verduras)    

    texto_Título_Sección_Pescados=ft.Text(value="sección de Pescados", color="black", size=20)
    page.add(texto_Título_Sección_Pescados)
    dropDownMenúPescados = ft.Dropdown(width=400, options=[ft.dropdown.Option("Almejas 20$/kg"),
                                                    ft.dropdown.Option("Sardinas  50$/kg"),
                                                    ft.dropdown.Option("Calamares 50$/kg"),
                                                    ft.dropdown.Option("Gambones  100$/kg"),
                                                    ft.dropdown.Option("Aleta de Tiburón 5000$/kg"),
                                                    ft.dropdown.Option("Atún Rojo 100.000.$/kg")])
    fila2 = ft.Row(spacing=0, controls=[dropDownMenúPescados,botón_Añadir_Pescados] )                                             
    page.add(fila2)
    slider_Kilos_Pescados=ft.Slider(min=0, max=5000,divisions=5000, label="Gramos{value}")
    page.add(slider_Kilos_Pescados)
    


    texto_Título_Sección_Carnes=ft.Text(value="sección de Carnes", color="black", size=20)
    page.add(texto_Título_Sección_Carnes)
    dropDownMenúCarnes = ft.Dropdown(width=400, options=[ft.dropdown.Option("Pechiga 10$/kg"),
                                                    ft.dropdown.Option("rabo de Toro 50$/kg"),
                                                    ft.dropdown.Option("Carne de Hereford 75$/kg"),
                                                    ft.dropdown.Option("Carne de Angus 100$/kg"),
                                                    ft.dropdown.Option("Carne de Ozaki 50.000$/kg"),
                                                    ft.dropdown.Option("Carne de Kobe 1000.000$/kg")])
    fila3 = ft.Row(spacing=0, controls=[dropDownMenúCarnes,botón_Añadir_Carnes] )                                             
    page.add(fila3)
    slider_Kilos_Carnes=ft.Slider(min=0, max=5000,divisions=5000, label="Gramos{value}")
    page.add(slider_Kilos_Carnes)
    


    texto_Título_Sección_Sales=ft.Text(value="sección de Sales", color="black", size=20)
    page.add(texto_Título_Sección_Sales)
    dropDownMenúSales = ft.Dropdown(width=400, options=[ft.dropdown.Option("Sal marina 1$/kg"),
                                                    ft.dropdown.Option("Sal yodada 1$/kg"),
                                                    ft.dropdown.Option("Sal gruesa o para hornear 1$/kg"),
                                                    ft.dropdown.Option("Sal del Himalaya o sal rosa 10$/kg"),
                                                    ft.dropdown.Option("Sal negra de Hawái 20$/kg"),
                                                    ft.dropdown.Option("Sal ahumada 30$/kg")])
    fila4 = ft.Row(spacing=0, controls=[dropDownMenúSales,botón_Añadir_Sales] )                                             
    page.add(fila4)
    slider_Kilos_Sales=ft.Slider(min=0, max=5000,divisions=5000, label="Gramos{value}")
    page.add(slider_Kilos_Sales)


    texto_Título_Sección_Cervezas=ft.Text(value="sección de Cervezas", color="black", size=20)
    page.add(texto_Título_Sección_Cervezas)
    dropDownMenúCervezas = ft.Dropdown(width=400, options=[ft.dropdown.Option("Mahou 1$/unidad"),
                                                    ft.dropdown.Option("Cruzcampo 1$/unidad"),
                                                    ft.dropdown.Option("Estrella Galicia 10$/unidad"),
                                                    ft.dropdown.Option("Alhambra 10$/unidad"),
                                                    ft.dropdown.Option("Salto Stout 20$/unidad"),
                                                    ft.dropdown.Option("Heineken 30$/unidad")])
    fila5 = ft.Row(spacing=0, controls=[dropDownMenúCervezas,botón_Añadir_Cervezas] )                                             
    page.add(fila5)
    slider_Cervezas=ft.Slider(min=0, max=50,divisions=50, label="Unidades{value}")
    page.add(slider_Cervezas)
    

    texto_Título_Sección_Botellas=ft.Text(value="sección de Botellas", color="black", size=20)
    page.add(texto_Título_Sección_Botellas)
    dropDownMenúBotellas = ft.Dropdown(width=400, options=[ft.dropdown.Option("Barcelo 12$/unidad"),
                                                    ft.dropdown.Option("Bombay 20$/unidad"),
                                                    ft.dropdown.Option("Beefeter 150$/unidad"),
                                                    ft.dropdown.Option("champagne Francés 80$/unidad"),
                                                    ft.dropdown.Option("Jageer 20$/unidad"),
                                                    ft.dropdown.Option("Tequila 30$/unidad")])
    fila6 = ft.Row(spacing=0, controls=[dropDownMenúBotellas,botón_Añadir_Botellas] )                                             
    page.add(fila6)
    slider_Botellas=ft.Slider(min=0, max=50,divisions=50, label="Unidades{value}")
    page.add(slider_Botellas)



    fila7 = ft.Row(spacing=250, controls=[botón_Finalizar_Compra] )                                             
    page.add(fila7)
        



ft.app(target=main)