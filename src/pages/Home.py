from flet import Text, Column, Page

class Home:
    def __init__(self, page: Page):
        self.page = page
        
        
    def render(self):
        return Column(
            controls=[
                Text("Hello, World!")   
            ]
        )
        
        
        
    