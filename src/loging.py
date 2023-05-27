import flet as ft

HEIGHT = 650
WIDTH = 615
BORDER_RADIUS = 15
PADDING = 5

class LogIn:
    def __init__(self, page: ft.Page):
        self.page = page
        main_container, extra_contanier= self.mainContainers()
        self.page.add(ft.Row([extra_contanier, main_container]))
        self.page.update()

    def mainContainers(self):
        self.login_container = ft.Container(
            width=WIDTH,
            height=HEIGHT,
            border_radius=BORDER_RADIUS,
            padding=PADDING,
            bgcolor=ft.colors.LIGHT_GREEN_600,
            content=ft.Text("Welcome to EcoSort",
                            size=30,
                            color="white",
                            weight=ft.FontWeight.BOLD,
                            text_align=ft.TextAlign.CENTER
            )
        )

        self.extra_container = ft.Container(
            width=WIDTH,
            height=HEIGHT,
            border_radius=BORDER_RADIUS,
            padding=PADDING,
            bgcolor=ft.colors.GREEN_500
        )

        return self.login_container, self.extra_container
