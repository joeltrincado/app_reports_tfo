import flet as ft
from components.Submenu import Submenu_

class MenuBar_(ft.UserControl):
    def __init__(self):
        pass

    def create(self):
        return ft.MenuBar(
        expand=True,
        style=ft.MenuStyle(
            alignment=ft.alignment.top_left,
            bgcolor="#19647E",
            mouse_cursor={
                ft.ControlState.HOVERED: ft.MouseCursor.WAIT,
                ft.ControlState.DEFAULT: ft.MouseCursor.ZOOM_OUT,
            },
        ),
        controls=[
            ft.SubmenuButton(
                content=ft.Text("Crear", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
                controls=[
                    Submenu_(content="Nueva Poliza", leading=ft.Icon(ft.Icons.ADD_BOX_ROUNDED), on_click=lambda _: print('Nueva Poliza')).create(),
                    Submenu_(content="Nueva Servicio", leading=ft.Icon(ft.Icons.MISCELLANEOUS_SERVICES_OUTLINED), on_click=lambda _: print('Nueva Servicio')).create(),
                ],
            ),
            ft.SubmenuButton(
                content=ft.Text("Datos", color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD),
                controls=[
                    Submenu_(content="Todos los registros", leading=ft.Icon(ft.Icons.APP_REGISTRATION_SHARP), on_click=lambda _: print('Todos los registros')).create(),
                    Submenu_(content="Clientes", leading=ft.Icon(ft.Icons.STREETVIEW), on_click=lambda _: print('Clientes')).create(),
                ],
            ),
        ],
    )