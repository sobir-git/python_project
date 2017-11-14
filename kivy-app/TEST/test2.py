from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import csv
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton

Builder.load_file('test2.kv')
class MangaListButton(ListItemButton):
    mangaList= ['naruto', 'bleach', 'one piece']
    pass
class RootWidget(BoxLayout):
    name_input = ObjectProperty()
    url_input = ObjectProperty()
    manga_list = ObjectProperty()
    def submit_manga(self):
        # Get the student name from the TextInputs
        manga_name = self.name_input.text + " " + self.url_input.text
        new_name= self.name_input.text
        new_url= self.url_input.text
        new_row=[new_name, new_url]
        # Add the student to the ListView
        self.manga_list.adapter.data.extend([manga_name])
 
        # Reset the ListView
        self.manga_list._trigger_reset_populate()
        with open('library.csv', 'a', newline='') as csvfile:
            #print(header)
            fileUpdate= csv.writer(csvfile)
            fileUpdate.writerow(new_row)
 
    def delete_manga(self, *args):
 
        # If a list item is selected
        if self.manga_list.adapter.selection:
 
            # Get the text from the item selected
            selection = self.manga_list.adapter.selection[0].text
 
            # Remove the matching item
            self.manga_list.adapter.data.remove(selection)
 
            # Reset the ListView
            self.manga_list._trigger_reset_populate()
 
    def replace_manga(self, *args):
 
        # If a list item is selected
        if self.manga_list.adapter.selection:
 
            # Get the text from the item selected
            selection = self.manga_list.adapter.selection[0].text
 
            # Remove the matching item
            self.manga_list.adapter.data.remove(selection)
 
            # Get the student name from the TextInputs
            manga_name = self.name_input.text + " " + self.url_input.text
 
            # Add the updated data to the list
            self.manga_list.adapter.data.extend([manga_name])
 
            # Reset the ListView
            self.manga_list._trigger_reset_populate()


class MainApp(App):
    def build(self):
        return RootWidget()

application= MainApp()
application.run()

