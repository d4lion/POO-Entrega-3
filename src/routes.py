from flet import Page

# Pages
from pages.Home import Home

def get(page: Page = None):
    return [
        {
            'path': '/',
            'title': 'Home',
            'component': Home(page)
        }
]