from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import csv
Builder.load_file('test2.kv')

class RootWidget(FloatLayout):

    def __init__(self, **kw):
        super(RootWidget, self).__init__(**kw)
        testList= ['potato', 'jake', 'ofu', 'zach']
        testlist = open("C:/Users/zfarley/Documents/Development/python_project/kivy-app/TEST/zachList.csv").read()
        #reads in data
        zach_list = testlist.split("\n")
        #print (zach_list)
        rows= 1
        for value in testList:
            btn= Button(text= str(value))
            self.ids.grid.add_widget(btn)
        pass


class MainApp(App):

    def build(self):
        return RootWidget()

if __name__ == '__main__':
    MainApp().run()



    """
    <GridLayout>
    canvas.before:
        Color:
            rgba: 0, 0, 0, 1
        BorderImage:
            # BorderImage behaves like the CSS BorderImage
            border: 10, 10, 10, 10
            source: '../examples/widgets/sequenced_images/data/images/button_white.png'
            pos: self.pos
            size: self.size

<RootWidget>
    
    GridLayout:
        size_hint: .9, .9
        pos_hint: {'center_x': .5, 'center_y': .5}
        rows:1
        Label:
            text: "I don't suffer from insanity, I enjoy every minute of it"
            text_size: self.width-20, self.height-20
            valign: 'top'
        Label:
            text: "When I was born I was so surprised; I didn't speak for a year and a half."
            text_size: self.width-20, self.height-20
            valign: 'middle'
            halign: 'center'
        Label:
            text: "A consultant is someone who takes a subject you understand and makes it sound confusing"
            text_size: self.width-20, self.height-20
            valign: 'bottom'
            halign: 'justify'
            """