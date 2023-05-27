import flet as ft

class LogIn:
    def __init__(self, page: ft.Page):
        self.page = page
        output_text = ft.Text("HOLA", size=32, text_align="start")
        self.page.add(output_text)
        self.page.update()
