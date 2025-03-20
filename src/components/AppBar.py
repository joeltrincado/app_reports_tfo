import flet as ft
from helpers import list_active_printers


class AppBar_():
    def __init__(self, onchange):
        self.printer = "" 
        self.printers = list_active_printers()
        self.printers_list = [ft.dropdown.Option(i) for i in self.printers]
        self.on_change = onchange        

    def create(self):

        return ft.AppBar(
            elevation=1,
            leading_width=50,
            toolbar_height=60,
            bgcolor= ft.Colors.GREY_300,
            title=ft.Text(
                spans=[
                    ft.TextSpan(
                        "TFO 1 JIMENEZ SPR DE RL DE CV",
                        ft.TextStyle(
                            size=20,
                            weight=ft.FontWeight.BOLD,
                            foreground=ft.Paint(
                                gradient=ft.PaintLinearGradient(
                                    (0, 200), (400, 200), ["#000000", "#000010"]
                                )
                            ),
                            font_family="times new roman",
                        ),
                    ),
                ],
            ),
            actions=[
                ft.Container(
                    content=ft.Dropdown(
                        options=self.printers_list,
                        on_change=self.on_change,    
                        value=self.printer,
                        label="Selecciona Impresora",
                        width=300,
                    ),padding=ft.padding.only(right=10)
                ),
            ]
        )