import flet as ft

class Container_(ft.Container):
    def __init__(self, content, w):
        self.content = content
        self.w = w

    def create(self):
        return ft.Container(content=self.content, padding=20, alignment=ft.alignment.center, border_radius=5, bgcolor="#1F2041", margin=20, width=self.w)