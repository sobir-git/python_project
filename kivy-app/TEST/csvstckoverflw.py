"""This code was found on stackoverflow and will be used for it's file handling system
to further develop the main APP mangaAPPv1.py. Current files used is csvstckoverflw.kv
*NOTE: file doesn't currently work properly but will still be analyzed later for functionality"""

import csv
import os
import easygui
import kivy
kivy.require('1.0.7')
from kivy.lang import Builder

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

Builder.load_file('csvstckoverflw.kv')

def csvImport(filename):
    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        your_list = list(reader)
        return your_list

class LoadFile(App):
    def FileLoadScreen(self):
        self.add_widget(Button(size_hint_y=(None), height=('48dp'), text='Select File',
        on_press=self.ImportFile))

    def ImportFile(self, instance):
        filepath = easygui.fileopenbox()
        if filepath!='.':
            a=csvImport(filepath)
            instance.text='File Loaded'
            instance.disabled=True

class loginBAKApp(App):
    def logAuth(username,password):
        if username!='' and password!='':
            print('ok')
    

if __name__ == '__main__':
    loginBAKApp().run()