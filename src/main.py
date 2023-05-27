import flet as ft
from loging import LogIn

def main(page: ft.Page):
    page.title = "EcoSort"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    LogIn(page)

ft.app(target=main)