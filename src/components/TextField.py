import flet as ft

class TextField_():
    def __init__(self, text, w, onchange):
        self.text = text
        self.w = w
        self.onchange = onchange

    def create(self):
        return ft.TextField(width=self.w,label=self.text, border_color=ft.colors.BLACK54,expand=True, on_change=lambda e: self.onchange(e))