import flet as ft
from flet.auth.providers.github_oauth_provider import GitHubOAuthProvider
import os

HEIGHT = 812
WIDTH = 375
BORDER_RADIUS = 15
PADDING = 5

class LogIn:
    def __init__(self, page: ft.Page):
        self.page = page
        self.main_container = self.mainContainers()
        self.page.add(self.main_container)
        self.page.update()

    def mainContainers(self):
        self.login_container = ft.Container(
            width=WIDTH,
            height=HEIGHT,
            border_radius=BORDER_RADIUS,
            padding=PADDING,
            bgcolor=ft.colors.LIGHT_GREEN_600
        )
    
        self.main_column = ft.Column(
            spacing=2,
            scroll="auto",
            alignment="start"
        )

        self.extra_container = ft.Container(
            width=WIDTH,
            height=HEIGHT*0.30,
            border_radius=BORDER_RADIUS,
            padding=PADDING,
            bgcolor=ft.colors.GREEN_500,
            on_click=self.button_actions
        )
        self.main_column.controls.append(self.extra_container)
        self.login_container.content = self.main_column

        return self.login_container

    def providers(self):
        self.github_provider = GitHubOAuthProvider(
                client_id=os.getenv("GITHUB_CLIENT_ID"),
                client_secret=os.getenv("GITHUB_CLIENT_SECRET"),
                redirect_url="http://localhost:8550/api/oauth/redirect",
                )

    def button_actions(self,e):
        print("HOLA")
    
    def buttons(self):
        self.github_button = ft.ElevatedButton("Login with GitHub", 
                                        on_click=self.button_actions,
                                        )
        return self.github_button
