from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.core.window import Window
from kivy.properties import ObjectProperty
import csv



Builder.load_file('test3.kv')

class Test(BoxLayout):
    name_input = ObjectProperty()
    url_input = ObjectProperty()
    manga_list = ObjectProperty()
    def __init__(self, **kw):
        super(Test, self).__init__(**kw)
        #self.bind(minimum_height=self.setter('height'))
        testlist = open("C:/Users/zfarley/Documents/Development/python_project/kivy-app/PROD/library.csv").read()
        #reads in data
        zach_list = testlist.split("\n")
        new_list=[]
        item_count= 1
        for value in zach_list:
            new_item=value.split(",")
            new_list.append(new_item)
        for pos in new_list:
            
            btn= Button(text= str(pos[0]), size_hint_y= None, height=40)
            label= Label(text=str(pos[1]) )
            #label_summary= Label(text=str(pos[2]), text_size=self.size)
            item_count= item_count + 1
            #self.rows= rows
            self.ids.grid.add_widget(label)
            self.ids.grid.add_widget(btn)
            #self.ids.grid.add_widget(label_summary)

    def submit_manga(self):
        # Get the student name from the TextInputs
        manga_name = self.name_input.text
        new_name= self.name_input.text
        new_url= self.url_input.text
        new_row=[new_name,new_url]
        print(new_row)
        with open('C:/Users/zfarley/Documents/Development/python_project/kivy-app/PROD/library.csv', 'a', newline='\n') as csvfile:
            fileUpdate= csv.writer(csvfile)
            #fileUpdate.writerow('\n')
            fileUpdate.writerow(new_row)      

class TestApp(App):
    def build(self):
        return Test()

TestApp().run()