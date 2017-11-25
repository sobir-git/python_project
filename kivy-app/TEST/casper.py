"""This code was found online and will be used as a source for learning about kivy screenmanagement. The needed files for this
app to function is casper.csv"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import os
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
import csv

Builder.load_string('''
<MenuScreen>:
    BoxLayout:
        Button:
            text: 'Add New Employee'
            on_press: root.manager.current = 'add_staff'
        Button:
            text: 'View Employee Profile'
            on_press: root.manager.current = 'read_staff'
        Button:
            text: 'Salary report'


<read_New_staff>:
    # nam: str(name_input)
    # job: job_input
    GridLayout:
        cols: 2
        Label:
            id: label
            font_size: 24
            bold: True
            height: root.height * .9
            size_hint_y: None
            # text: "file Content show here....."
            text_size: self.width, None
            height: self.texture_size[1]
            valign: 'middle'
            halign: 'center'

        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
        Button:
            text: 'Show Data'
            on_press: app.show()

<Lay>:
    cols: 1
    label: label
    padding: 20
    Label:
        height: root.height * .1
        size_hint_y: None
        text: 'Read what is below'
        font_size: 24
        bold: True
    ScrollView:
        height: root.height * .85
        size_hint_y: None
        Label:
            id: label
            font_size: 24
            bold: True
            height: root.height * .9
            size_hint_y: None
            text: 'we will rock you'
            text_size: self.width, None
            height: self.texture_size[1]
            # valign: 'middle'
            # halign: 'center'


<Add_new_staff>:
    # nam: str(name_input)
    # job: job_input
    GridLayout:
        cols: 2
        Label:
            text: 'Product Name'
        TextInput:
            id: name_input
        Label:
            text: 'Price'
        TextInput:
            id: price_input
        Label:
            text: 'Priority'
        TextInput:
            id: priority_input
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
        Button:
            text: 'Save'
            on_press: app.save(name_input.text, price_input.text,priority_input.text)
''')


class MenuScreen(Screen):
    pass

class Add_new_staff(Screen):
    pass

class read_New_staff(Screen):
    pass

class Lay(GridLayout):
    label = ObjectProperty()

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(Add_new_staff(name='add_staff'))
sm.add_widget(read_New_staff(name='read_staff'))


class TestApp(App):
    def build(self):
        l = Lay()
        fob = open('TEST/casper.csv','r')
        content = fob.read()
        fob.close()
        l.label.text = content
        self.hello = Button(text = "hello")
        self.hello.bind(on_press = self.show)       
        return sm  #l

    def save(self, name,price,priority):
        fob = open('TEST/casper.csv','a')
        fob.write("Product Name:- " + name + "\n")
        fob.write("Price:- " + price + "\n")
        fob.write("Priority:- " + priority + "\n")
        fob.write("--------------------\n")
        fob.close()    

    def show(self, *args):
        l = Lay()
        fob = open('TEST/casper.csv','r')
        content = fob.read()
        fob.close()
        # l.label.text = content
        print(content)
#Look at this page: https://stackoverflow.com/questions/42748343/how-to-show-csv-file-in-a-grid



if __name__ == '__main__':
    TestApp().run()
    # NewApp().run()