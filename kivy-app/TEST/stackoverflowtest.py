from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.core.window import Window
import csv



Builder.load_string("""

<Test>:
    orientation: "vertical"
    padding: 10
    spacing: 10
    BoxLayout:
        size_hint_y:None
        height: "40dp"
        Label:
            text: 'Name'
        TextInput:
            id: name
        Label:
            text: 'Weblink'
        TextInput:
            id: url
    BoxLayout:
        size_hint_y:None
        height: "40dp"
        Button:
            text: 'Submit'
            size_hint_x: 15
            on_press: root.submit_manga()
        Button:
            text: 'Delete'
            size_hint_x: 15
            on_press: root.delete_manga()

        Button:
            text: 'Replace'
            size_hint_x: 15
            on_press: root.replace_manga()

    ScrollView:
        size_hint: (1, 1)
        height: 50
        
        GridLayout:
            id: grid
            size_hint_y: None
            size_hint_x: 1
            height: self.minimum_height
            cols: 3
            Label:
                text:'col 1'
            Label:
                text:'col 2'
            Label: 
                text: 'col 3'
"""
)

class Test(BoxLayout):
    label_value = ListProperty()
    testList= ['potato', 'jake', 'ofu', 'zach']
    def __init__(self, **kw):
        super(Test, self).__init__(**kw)
        #self.bind(minimum_height=self.setter('height'))
        testlist = open("C:/Users/zfarley/Documents/Development/python_project/kivy-app/TEST/zachList.csv").read()
        #reads in data
        zach_list = testlist.split("\n")
        new_list=[]
        item_count= 1
        for value in zach_list:
            new_item=value.split(",")
            new_list.append(new_item)
        for pos in new_list:
            
            btn= Button(text= str(pos[1]), size_hint_y= None, height=40)
            label= Label(text=str(pos[0]) )
            label_summary= Label(text=str(pos[2]), text_size=self.size)
            item_count= item_count + 1
            #self.rows= rows
            self.ids.grid.add_widget(label)
            self.ids.grid.add_widget(btn)
            self.ids.grid.add_widget(label_summary)
                

class TestApp(App):
    def build(self):
        return Test()

TestApp().run()