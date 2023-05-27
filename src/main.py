import flet as ft
from loging import LogIn

HEIGHT = 812
WIDTH = 375
BORDER_RADIUS = 15
PADDING = 5

def main(page: ft.Page):
    page.title = "EcoSort"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.window_full_screen = False
    page.bgcolor = ft.colors.LIGHT_GREEN_400
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    LogIn(page)

ft.app(target=main)