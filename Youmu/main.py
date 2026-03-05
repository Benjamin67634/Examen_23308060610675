import flet as ft

def main(page: ft.Page):
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.title = "Examen Final - Registro de Participantes"
    
    page.add(ft.Text(
        text_align=ft.TextAlign.CENTER,
        value="Registro de participantes",
        size=30,
        weight=ft.FontWeight.BOLD,
    ))

    txt_correo = page.add(ft.TextField(
        label="Correo electronico",
    ))
    txt_nombre = page.add(ft.TextField(
        label="Nombre completo",
    ))
    
    drop_interes= page.add(ft.Dropdown(
        label="Taller de interés",
        options=[
        ft.DropdownOption(key="Python para Principiantes", text="Python para Principiantes"),
        ft.DropdownOption(key="Flet Intermedio", text="Flet Intermedio"),
        ft.DropdownOption(key="Análisis de Datos con Pandas", text="Análisis de Datos con Pandas"),
     ],
    ))
    

    group_pago = page.add(ft.RadioGroup(
        content=ft.Row([
        ft.Text("Metodo de pago"),
        ft.Radio(value="Pago completo", label="Pago completo"),
        ft.Radio(value="Pago por cuotas", label="Pago por cuotas"),
    ]),
    ))
    
    chck_lap= page.add(ft.Checkbox(
        label="Requiere computadora portatil",
        value=False,
        tristate=False,
    ))
    
    slider= page.add(
        ft.Text("Nivel de experiencia"),
        ft.Slider(min=0, max=50, divisions=5, label="{value}%"),
    )
    button_resumen= page.add(ft.Button(
    content="Mostrar Ficha del Participante",
    icon=ft.Icons.SAVE,
    icon_color=ft.Colors.WHITE,
    color=ft.Colors.WHITE,
    bgcolor=ft.Colors.BLUE,
    elevation=5,
    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
       ) )
    
    
    
    
    
    page.add(
        ft.Row(
            [
                
            ],
        )
    ) 
ft.run(main)