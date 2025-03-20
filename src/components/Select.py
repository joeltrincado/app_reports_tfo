import flet as ft

class Select_():
    def __init__(self, onChange, w):
        self.onChange = onChange
        self.w = w
        


    def create(self):
        return ft.Dropdown(
            options=[
                ft.dropdown.Option("10 %"),
                ft.dropdown.Option("20 %"),
                ft.dropdown.Option("30 %"),
                ft.dropdown.Option("40 %"),
            ],
            on_change=self.onChange,
            hint_content="Selecciona la utilidad",
            value="10",
            label="Utilidad",
            width=self.w,

        )