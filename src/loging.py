import flet as ft

HEIGHT = 650
WIDTH = 615

class LogIn:
    def __init__(self, page: ft.Page):
        self.page = page
        main_container, extra_contanier = self.loginContainer()
        self.page.add(ft.Row([main_container, extra_contanier]))
        self.page.update()

    def loginContainer(self):
        login = ft.Container(
            width=WIDTH,
            height=HEIGHT,
            border_radius=35,
            padding=5,
            # bgcolor="green"
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_right,
                end=ft.alignment.bottom_right,
                colors=['brown']
                )
        )

        extra = ft.Container(
            width=WIDTH,
            height=HEIGHT,
            border_radius=35,
            padding=5,
            # bgcolor="green"
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_left,
                colors=['green']
                )
        )

        return login, extra
