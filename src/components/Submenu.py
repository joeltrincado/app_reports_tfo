import flet as ft

class Submenu_():
    def __init__(self, content:str, leading:ft.Icons, on_click=lambda _: print('Submenu')):
        self.content = content
        self.leading = leading
        self.on_click = on_click
    
    def create(self):
        return ft.MenuItemButton(
                        content=ft.Text(value=self.content),
                        leading=self.leading,
                        style=ft.ButtonStyle(
                            bgcolor={ft.ControlState.HOVERED: "#1F2041"},
                            color={ft.ControlState.HOVERED: ft.Colors.WHITE},
                            icon_color={ft.ControlState.HOVERED: ft.Colors.WHITE},
                            shape={ft.ControlState.HOVERED: ft.RoundedRectangleBorder(radius=0)},
                        ),
                        on_click=self.on_click,
                    )