from kivy.app import App
from src.Form import Form 

class MyClass(App):
    def build(self):
        app = Form()
        return app
