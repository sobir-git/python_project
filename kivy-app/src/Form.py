from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.graphics import Color
from kivy.uix.widget import Widget

class Form(GridLayout):
    def __init__(self, **kwargs):
        self.cols = 2
        self.rows = 3
        self.background_color = Color(1, 1, 1)

        nameLabel = Label(text='Name', pos=(100, 100))
        genreLabel = Label(text='Genre', pos=(100, 90))
        summaryLabel = Label(text='Summary', pos=(100, 80))
        self.add_widget(nameLabel)
        self.add_widget(genreLabel)
        self.add_widget(summaryLabel)

        super(Form, self).__init__(**kwargs)

