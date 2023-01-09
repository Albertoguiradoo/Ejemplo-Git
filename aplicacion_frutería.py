import flet as ft


def main(page: ft.Page):
    page.title="Bienvenido a su frutería de confianza!"
    caja_número_1= ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)
    caja_número_2= ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)
    caja_número_3= ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)
    caja_número_4= ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)
    caja_número_5= ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)
    def minus_click(e):
        caja_número_1.value = str(int(caja_número_1.value) - 1)
        caja_número_2.value = str(int(caja_número_2.value) - 1)
        caja_número_3.value = str(int(caja_número_3.value) - 1)
        caja_número_4.value = str(int(caja_número_4.value) - 1)
        caja_número_5.value = str(int(caja_número_5.value) - 1)
        
        page.update()

    def plus_click(e):
        caja_número_1.value = str(int(caja_número_1.value) + 1)
        caja_número_2.value = str(int(caja_número_2.value) + 1)
        caja_número_3.value = str(int(caja_número_3.value) + 1)
        caja_número_4.value = str(int(caja_número_1.value) + 1)
        caja_número_5.value = str(int(caja_número_5.value) + 1)
        
        page.update()

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
    page.add(
        ft.Row(
            [ft.IconButton(ft.icons.REMOVE, on_click=minus_click),caja_número_1,
            ft.IconButton(ft.icons.ADD, on_click=plus_click)],
            alignment=ft.MainAxisAlignment.CENTER))
    
    
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
    page.add(
        ft.Row(
            [ft.IconButton(ft.icons.REMOVE, on_click=minus_click),caja_número_2,
            ft.IconButton(ft.icons.ADD, on_click=plus_click)],
            alignment=ft.MainAxisAlignment.CENTER))
    


    


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
    page.add(
        ft.Row(
            [ft.IconButton(ft.icons.REMOVE, on_click=minus_click),caja_número_3,
            ft.IconButton(ft.icons.ADD, on_click=plus_click)],
            alignment=ft.MainAxisAlignment.CENTER))
    
 

   
    texto_Título_Sección_Cervezas=ft.Text(value="sección de Cervezas", color="black", size=20)
    page.add(texto_Título_Sección_Cervezas)
    dropDownMenúCervezas = ft.Dropdown(width=400, options=[ft.dropdown.Option("Mahou 1$/unidad"),
                                                    ft.dropdown.Option("Cruzcampo 1$/unidad"),
                                                    ft.dropdown.Option("Estrella Galicia 10$/unidad"),
                                                    ft.dropdown.Option("Alhambra 10$/unidad"),
                                                    ft.dropdown.Option("Salto Stout 20$/unidad"),
                                                    ft.dropdown.Option("Heineken 30$/unidad")])
    fila4 = ft.Row(spacing=0, controls=[dropDownMenúCervezas,botón_Añadir_Cervezas] )                                             
    page.add(fila4)
    page.add(
        ft.Row(
            [ft.IconButton(ft.icons.REMOVE, on_click=minus_click),caja_número_4,
            ft.IconButton(ft.icons.ADD, on_click=plus_click)],
            alignment=ft.MainAxisAlignment.CENTER))
    
   
    

    texto_Título_Sección_Botellas=ft.Text(value="sección de Botellas", color="black", size=20)
    page.add(texto_Título_Sección_Botellas)
    dropDownMenúBotellas = ft.Dropdown(width=400, options=[ft.dropdown.Option("Barcelo 12$/unidad"),
                                                    ft.dropdown.Option("Bombay 20$/unidad"),
                                                    ft.dropdown.Option("Beefeter 150$/unidad"),
                                                    ft.dropdown.Option("champagne Francés 80$/unidad"),
                                                    ft.dropdown.Option("Jageer 20$/unidad"),
                                                    ft.dropdown.Option("Tequila 30$/unidad")])
    fila5 = ft.Row(spacing=0, controls=[dropDownMenúBotellas,botón_Añadir_Botellas] )                                             
    page.add(fila5)
    page.add(
        ft.Row(
            [ft.IconButton(ft.icons.REMOVE, on_click=minus_click),caja_número_5,
            ft.IconButton(ft.icons.ADD, on_click=plus_click)],
            alignment=ft.MainAxisAlignment.CENTER))


    #slider_Botellas=ft.Slider(min=0, max=50,divisions=50, label="Unidades{value}")
    #page.add(slider_Botellas)



    fila6 = ft.Row(spacing=250, controls=[botón_Finalizar_Compra] )                                             
    page.add(fila6)
        
     

    



ft.app(target=main)