import flet as ft

def main(page):

    title = ft.Text(value="Welcome to EcoSort!",
                    font_family="Consolas",
                    size=72,
                    text_align= ft.TextAlign.CENTER)
    
    boton = ft.ElevatedButton("Hola")

    def btn_click(e):
        pass

    page.add(
        title,boton,
    )

ft.app(target=main, view=ft.WEB_BROWSER)